#!python
import requests
import yaml
import random
import sys
import os
import json
import xml.etree.ElementTree as ET
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup


# def fetch_arxiv_metadata(arxiv_id):
#     """Fetch metadata from arXiv."""
#     url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise Exception(f"Failed to fetch metadata for {arxiv_id}.")

#     # Parse XML response
#     root = ET.fromstring(response.content)
#     entry = root.find("{http://www.w3.org/2005/Atom}entry")
#     if entry is None:
#         raise Exception(f"No entry found for arXiv ID {arxiv_id}.")

#     # Extract title
#     title = entry.find("{http://www.w3.org/2005/Atom}title")
#     if title is None or not title.text:
#         raise Exception(f"Failed to parse title for arXiv ID {arxiv_id}.")

#     # Extract authors
#     authors = []
#     for author in entry.findall("{http://www.w3.org/2005/Atom}author"):
#         name = author.find("{http://www.w3.org/2005/Atom}name")
#         if name is not None and name.text:
#             authors.append(name.text.strip())

#     # Extract link to the paper
#     link = entry.find("{http://www.w3.org/2005/Atom}id")
#     if link is None or not link.text:
#         raise Exception(f"Failed to find URL for arXiv ID {arxiv_id}.")

#     # Extract published date (only date part)
#     published = entry.find("{http://www.w3.org/2005/Atom}published")
#     if published is None or not published.text:
#         raise Exception(f"Failed to find published date for arXiv ID {arxiv_id}.")
#     published_date = published.text.strip().split("T")[0]  # Keep only the date part

#     return {
#         "arxiv_id": arxiv_id,
#         "title": title.text.strip(),
#         "authors": ", ".join(authors),
#         "url": link.text.strip(),
#         "published": published_date,
#     }

# ---------------------------
# Helpers: detection & parsing
# ---------------------------

_ARXIV_ID_RE = re.compile(r"^(?:arXiv:)?\d{4}\.\d{4,5}(?:v\d+)?$", re.IGNORECASE)

def _is_arxiv_id_or_url(s: str) -> bool:
    s = s.strip()
    if _ARXIV_ID_RE.match(s):
        return True
    try:
        u = urlparse(s)
        return u.netloc.endswith("arxiv.org") and (u.path.startswith("/abs/") or u.path.startswith("/pdf/"))
    except Exception:
        return False

def _normalize_arxiv_id(s: str) -> str:
    s = s.strip()
    if _ARXIV_ID_RE.match(s):
        return s.replace("arXiv:", "").lower()
    u = urlparse(s)
    # /abs/<id>[.pdf], /pdf/<id>.pdf
    parts = u.path.split("/")
    try:
        idx = parts.index("abs")
        raw = parts[idx + 1]
    except ValueError:
        # maybe /pdf/<id>.pdf
        idx = parts.index("pdf")
        raw = parts[idx + 1].replace(".pdf", "")
    return raw.lower()

def _is_chemrxiv_url(s: str) -> bool:
    try:
        u = urlparse(s.strip())
        return u.netloc.endswith("chemrxiv.org")
    except Exception:
        return False

def _is_acs_url(s: str) -> bool:
    try:
        u = urlparse(s.strip())
        return u.netloc.endswith("pubs.acs.org") and "/doi/" in u.path
    except Exception:
        return False

def _is_openreview_url(s: str) -> bool:
    try:
        u = urlparse(s.strip())
        if not u.netloc.endswith("openreview.net"):
            return False
        # Check for common OpenReview URL patterns
        return (
            "/forum?id=" in u.path or 
            "/pdf?id=" in u.path or 
            "id=" in u.query or
            u.path.startswith("/forum/") or
            u.path.startswith("/pdf/")
        )
    except Exception:
        return False

def _is_nature_url(s: str) -> bool:
    try:
        u = urlparse(s.strip())
        return (
            u.netloc.endswith("nature.com") or 
            u.netloc.endswith("natures.com") or
            u.netloc.endswith(".nature.com")
        ) and "/articles/" in u.path
    except Exception:
        return False

def _extract_doi(s: str) -> str | None:
    """
    Return a DOI if `s` is a DOI or DOI URL; else None.
    """
    s = s.strip()
    # Bare DOI
    if s.lower().startswith("10."):
        return s
    # DOI URL forms
    m = re.search(r"(10\.\d{4,9}/\S+)", s)
    return m.group(1) if m else None

def _headers():
    return {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Cache-Control": "max-age=0",
    }

# ---------------------------
# arXiv
# ---------------------------

def fetch_arxiv_metadata(arxiv_id_or_url: str, timeout: int = 20) -> dict:
    """Fetch metadata from arXiv via the Atom API, normalized."""
    arxiv_id = _normalize_arxiv_id(arxiv_id_or_url)
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    response = requests.get(url, headers=_headers(), timeout=timeout)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch metadata for {arxiv_id}.")

    root = ET.fromstring(response.content)
    entry = root.find("{http://www.w3.org/2005/Atom}entry")
    if entry is None:
        raise Exception(f"No entry found for arXiv ID {arxiv_id}.")

    title_tag = entry.find("{http://www.w3.org/2005/Atom}title")
    if title_tag is None or not title_tag.text:
        raise Exception(f"Failed to parse title for arXiv ID {arxiv_id}.")
    title = title_tag.text.strip()

    authors = []
    for author in entry.findall("{http://www.w3.org/2005/Atom}author"):
        name = author.find("{http://www.w3.org/2005/Atom}name")
        if name is not None and name.text:
            authors.append(name.text.strip())

    link = entry.find("{http://www.w3.org/2005/Atom}id")
    if link is None or not link.text:
        raise Exception(f"Failed to find URL for arXiv ID {arxiv_id}.")
    url_abs = link.text.strip()

    published = entry.find("{http://www.w3.org/2005/Atom}published")
    if published is None or not published.text:
        raise Exception(f"Failed to find published date for arXiv ID {arxiv_id}.")
    published_date = published.text.strip().split("T")[0]

    # Try PDF link
    pdf_url = None
    for l in entry.findall("{http://www.w3.org/2005/Atom}link"):
        if l.attrib.get("title") == "pdf" or l.attrib.get("type") == "application/pdf":
            pdf_url = l.attrib.get("href")
            break

    return {
        "identifier": arxiv_id,
        "title": title,
        "authors": ", ".join(authors),
        "published": published_date,
    }

# ---------------------------
# ChemRxiv (HTML meta tags)
# ---------------------------

def fetch_chemrxiv_metadata(article_url: str, timeout: int = 20) -> dict:
    resp = requests.get(article_url, headers=_headers(), timeout=timeout)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch metadata for {article_url}")

    # Store raw HTML for regex fallback
    raw_html = resp.text
    
    soup = BeautifulSoup(raw_html, "html.parser")
    
    # Debug: Check if h1 exists at all
    all_h1s = soup.find_all("h1")
    if not all_h1s:
        # Try with lxml parser as fallback (handles malformed HTML better)
        try:
            soup = BeautifulSoup(raw_html, "lxml")
            all_h1s = soup.find_all("h1")
        except Exception:
            pass

    def _first(*cands):
        for kind, val in cands:
            if kind == "name":
                m = soup.find("meta", attrs={"name": val})
            else:
                m = soup.find("meta", attrs={"property": val})
            if m and m.get("content"):
                return m["content"].strip()
        return None

    # Try multiple strategies to find the title
    title = _first(
        ("name", "dc.title"),
        ("property", "og:title"),
        ("name", "citation_title"),
        ("property", "twitter:title"),
    )
    
    # Fallback to HTML title tag
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            title_text = title_tag.get_text(strip=True)
            if title_text:
                title = title_text
                # Clean up title if it contains extra info (e.g., "Title | ChemRxiv")
                if "|" in title:
                    title = title.split("|")[0].strip()
    
    # Fallback to h1 tag (use get_text to handle nested structures)
    if not title:
        h1_tag = soup.find("h1")
        if h1_tag:
            title_text = h1_tag.get_text(separator=" ", strip=True)
            if title_text:
                title = title_text
    
    # Fallback to span with truncate-title class (ChemRxiv specific)
    if not title:
        title_span = soup.find("span", class_=re.compile("truncate.*title|title.*truncate", re.I))
        if title_span:
            title_text = title_span.get_text(separator=" ", strip=True)
            if title_text:
                title = title_text
    
    # Fallback: find any h1 and extract title from nested structure (ChemRxiv Vue.js rendered content)
    if not title:
        h1_tag = soup.find("h1")
        if h1_tag:
            # Strategy 1: Find span with truncate-title class (most specific for ChemRxiv)
            truncate_span = h1_tag.find("span", class_=lambda x: x and any("truncate" in str(c).lower() and "title" in str(c).lower() for c in x) if x else False)
            if truncate_span:
                title_text = truncate_span.get_text(separator=" ", strip=True)
                if title_text and len(title_text) > 10:
                    title = title_text
            
            # Strategy 2: Find any span inside h1 with substantial text (fallback)
            if not title:
                for span in h1_tag.find_all("span"):
                    span_text = span.get_text(separator=" ", strip=True)
                    # Filter out very short texts and common non-title text
                    if span_text and len(span_text) > 10 and not span_text.lower().startswith(("back to", "version", "march", "january", "february", "april", "may", "june", "july", "august", "september", "october", "november", "december")):
                        title = span_text
                        break
            
            # Strategy 3: Try to find div with article-header-title class
            if not title:
                for div in h1_tag.find_all("div"):
                    div_classes = div.get("class", [])
                    if div_classes and any("article-header-title" in str(c).lower() for c in div_classes):
                        # Look for span inside this div
                        span_in_div = div.find("span")
                        if span_in_div:
                            title_text = span_in_div.get_text(separator=" ", strip=True)
                            if title_text and len(title_text) > 10:
                                title = title_text
                                break
                        # If no span, try div text
                        div_text = div.get_text(separator=" ", strip=True)
                        if div_text and len(div_text) > 10:
                            title = div_text
                            break
            
            # Strategy 4: Get all text from h1 and use the longest substantial piece
            if not title:
                all_texts = [text.strip() for text in h1_tag.stripped_strings if text.strip() and len(text.strip()) > 10]
                if all_texts:
                    # Filter out dates and version strings
                    filtered_texts = [t for t in all_texts if not re.match(r'^\d{1,2}\s+\w+\s+\d{4}', t) and not t.lower().startswith("version")]
                    if filtered_texts:
                        # Use the longest text piece (likely the title)
                        title = max(filtered_texts, key=len)
                    elif all_texts:
                        title = max(all_texts, key=len)
    
    # Fallback to article-header-title class anywhere (not just in h1)
    if not title:
        # Try finding any element with article-header-title class using CSS selector
        try:
            title_elements = soup.select(".article-header-title")
        except Exception:
            title_elements = []
        # Fallback to lambda if CSS selector doesn't work
        if not title_elements:
            title_elements = soup.find_all(class_=lambda x: x and any("article-header-title" in str(c).lower() for c in x) if x else False)
        for elem in title_elements:
            # Look for span inside first
            span_in_elem = elem.find("span")
            if span_in_elem:
                title_text = span_in_elem.get_text(separator=" ", strip=True)
                if title_text and len(title_text) > 10:
                    title = title_text
                    break
            # If no span, use element text
            title_text = elem.get_text(separator=" ", strip=True)
            if title_text and len(title_text) > 10:
                title = title_text
                break
    
    # Fallback to JSON-LD structured data
    if not title:
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                script_content = script.string or script.get_text(strip=True)
                if not script_content:
                    continue
                data = json.loads(script_content)
                if isinstance(data, dict):
                    if "headline" in data:
                        title = data["headline"]
                    elif "name" in data:
                        title = data["name"]
                elif isinstance(data, list) and len(data) > 0:
                    item = data[0]
                    if isinstance(item, dict):
                        if "headline" in item:
                            title = item["headline"]
                        elif "name" in item:
                            title = item["name"]
                if title:
                    break
            except (json.JSONDecodeError, AttributeError, TypeError):
                continue
    
    # Final fallback: Try to extract from any visible text that looks like a title
    if not title:
        # Look for h1 tag and get ALL its text, then clean it up
        h1_tag = soup.find("h1")
        if h1_tag:
            full_text = h1_tag.get_text(separator=" ", strip=True)
            # Split by common separators and take the longest piece that looks like a title
            if full_text:
                # Remove HTML comments and split by multiple spaces/newlines
                parts = [p.strip() for p in re.split(r'\s{2,}|\n', full_text) if p.strip() and len(p.strip()) > 10]
                # Filter out date patterns and version info
                filtered = [p for p in parts if not re.match(r'^\d{1,2}\s+\w+\s+\d{4}', p, re.I) and not p.lower().startswith("version")]
                if filtered:
                    title = max(filtered, key=len)
                elif parts:
                    title = max(parts, key=len)
        
        # Last resort: try finding title in page title or any large text block
        if not title:
            page_title_tag = soup.find("title")
            if page_title_tag:
                page_title = page_title_tag.get_text(strip=True)
                # Remove site name suffixes
                for suffix in [" - ChemRxiv", " | ChemRxiv", " - Cambridge Open Engage"]:
                    if page_title.endswith(suffix):
                        page_title = page_title[:-len(suffix)].strip()
                if page_title and len(page_title) > 10:
                    title = page_title
    
    if not title:
        # Provide debug info in the error message
        available_meta = []
        for meta in soup.find_all("meta"):
            if meta.get("name"):
                available_meta.append(f"name={meta.get('name')}")
            if meta.get("property"):
                available_meta.append(f"property={meta.get('property')}")
        
        # Debug: Check what h1 contains
        h1_debug = "N/A"
        h1_tag = soup.find("h1")
        if h1_tag:
            h1_text = h1_tag.get_text(separator=" ", strip=True)[:200]
            h1_html = str(h1_tag)[:300]
            h1_debug = f"h1 found with text: {h1_text[:100]}... HTML: {h1_html[:150]}..."
        else:
            # Check if h1 exists at all in the response
            all_h1s = soup.find_all("h1")
            h1_debug = f"No h1 found (found {len(all_h1s)} h1 tags total)"
            # Try searching for "article-header-title" in raw HTML
            if "article-header-title" in raw_html:
                # Find the position
                idx = raw_html.find("article-header-title")
                snippet = raw_html[max(0, idx-100):idx+500]
                h1_debug += f". Found 'article-header-title' in HTML at position {idx}. Snippet: {snippet[:200]}..."
        
        # Also try a direct regex search on the raw HTML as absolute last resort
        # Use the raw HTML we stored at the beginning
        if not title and "article-header-title" in raw_html:
            # Try to extract title using regex from raw HTML
            import re as regex_module
            # Look for pattern like: <span ...>Title text</span> inside div with article-header-title
            # Pattern 1: <div class="...article-header-title..."><span>Title</span>
            pattern1 = r'<div[^>]*article-header-title[^>]*>.*?<span[^>]*>([^<]{10,})</span>'
            matches = regex_module.findall(pattern1, raw_html, regex_module.DOTALL | regex_module.IGNORECASE)
            if not matches:
                # Pattern 2: <span class="truncate-title">Title</span> inside h1
                pattern2 = r'<h1[^>]*>.*?<span[^>]*truncate-title[^>]*>([^<]{10,})</span>'
                matches = regex_module.findall(pattern2, raw_html, regex_module.DOTALL | regex_module.IGNORECASE)
            if not matches:
                # Pattern 3: Any span inside h1 that contains substantial text
                pattern3 = r'<h1[^>]*>.*?<span[^>]*>([^<]{15,})</span>'
                matches = regex_module.findall(pattern3, raw_html, regex_module.DOTALL | regex_module.IGNORECASE)
            if matches:
                # Clean up the match (remove HTML entities, extra whitespace)
                potential_title = matches[0].strip()
                # Remove HTML comments and normalize whitespace
                potential_title = regex_module.sub(r'<!--.*?-->', '', potential_title, flags=regex_module.DOTALL)
                potential_title = regex_module.sub(r'\s+', ' ', potential_title).strip()
                if len(potential_title) > 10:
                    title = potential_title
        
        if not title:
            raise Exception(
                f"Failed to parse title from ChemRxiv page {article_url}. "
                f"Available meta tags: {', '.join(available_meta[:10]) if available_meta else 'none'}. "
                f"{h1_debug}"
            )

    # Extract authors
    authors = [m.get("content").strip() for m in soup.find_all("meta", attrs={"name": "dc.creator"}) if m.get("content")]
    
    # Fallback: extract from visible HTML (ChemRxiv Vue.js rendered content)
    if not authors:
        author_links = soup.find_all("a", attrs={"data-test-id": "AuthorNameLink"})
        for link in author_links:
            author_text = link.get_text(strip=True)
            if author_text and len(author_text) > 2:
                authors.append(author_text)
    
    # Fallback: extract from embedded JSON data (Nuxt state)
    if not authors:
        for script in soup.find_all("script"):
            script_content = script.string or script.get_text(strip=True)
            if not script_content or "selectedItem" not in script_content:
                continue
            try:
                # Try to find JSON-like structure with authors
                # Look for patterns like "authors:[" or "firstName:"
                # Try to extract author names from the embedded state
                author_matches = re.findall(r'"(?:firstName|lastName)":"([^"]+)"', script_content)
                if author_matches:
                    # Combine first and last names (rough heuristic)
                    for i in range(0, len(author_matches) - 1, 2):
                        if i + 1 < len(author_matches):
                            full_name = f"{author_matches[i]} {author_matches[i+1]}"
                            authors.append(full_name)
                    if author_matches and len(author_matches) % 2 == 1:
                        authors.append(author_matches[-1])
                    if authors:
                        break
            except Exception:
                continue
    
    published = _first(("name", "dc.date"))
    if published:
        published = published.split("T")[0]
    
    # Fallback: try to extract published date from visible HTML or JSON
    if not published:
        # Look for date patterns in the page
        date_pattern = re.compile(r'(\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})', re.I)
        date_matches = date_pattern.findall(soup.get_text())
        if date_matches:
            # Use the first date found
            published = date_matches[0]
    doi = _first(("name", "dc.identifier"))
    abstract = _first(("name", "dc.description"), ("property", "og:description"))

    # Normalize DOI if dc.identifier is a URL
    if doi and doi.lower().startswith("http"):
        m = re.search(r"(10\.\d{4,9}/\S+)", doi)
        doi = m.group(1) if m else doi

    return {
        "identifier": article_url,
        "title": title,
        "authors": ", ".join(authors) if authors else "Unknown",
        "published": published or "Unknown",
    }

# ---------------------------
# ACS (HTML meta tags)
# ---------------------------

_ACS_PREFIXES = (
    "https://pubs.acs.org/doi/",
    "http://pubs.acs.org/doi/",
    "https://pubs.acs.org/doi/full/",
    "https://pubs.acs.org/doi/abs/",
)

def _normalize_acs_url(doi_or_url: str) -> str:
    s = doi_or_url.strip()
    if s.lower().startswith("10."):
        return f"https://pubs.acs.org/doi/{s}"
    if any(s.startswith(p) for p in _ACS_PREFIXES):
        return s
    if urlparse(s).netloc.endswith("pubs.acs.org"):
        return s
    raise ValueError(f"Not an ACS DOI or URL: {doi_or_url}")

def fetch_acs_metadata(doi_or_url: str, timeout: int = 20) -> dict:
    url = _normalize_acs_url(doi_or_url)
    resp = requests.get(url, headers=_headers(), timeout=timeout)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch page ({resp.status_code}) for {url}")

    soup = BeautifulSoup(resp.text, "html.parser")

    def get_all(name=None, prop=None):
        if name:
            return [m.get("content", "").strip() for m in soup.find_all("meta", attrs={"name": name}) if m.get("content")]
        if prop:
            return [m.get("content", "").strip() for m in soup.find_all("meta", attrs={"property": prop}) if m.get("content")]
        return []

    def first(*cands):
        for kind, val in cands:
            vals = get_all(name=val if kind == "name" else None, prop=val if kind == "property" else None)
            if vals:
                return vals[0]
        return None

    title = first(("name", "citation_title"), ("property", "og:title"), ("name", "dc.Title"), ("name", "dc.title"))
    if not title:
        raise Exception("Failed to parse title from ACS page.")

    authors = get_all(name="citation_author") or get_all(name="dc.Creator") or get_all(name="dc.creator")

    doi = first(("name", "citation_doi"), ("name", "dc.Identifier"), ("name", "dc.identifier")) or first(("name", "prism.doi"),)
    if doi and doi.lower().startswith("http"):
        m = re.search(r"(10\.\d{4,9}/\S+)", doi)
        doi = m.group(1) if m else doi

    published = first(("name", "citation_publication_date"), ("name", "prism.publicationDate"), ("name", "dc.Date"), ("name", "dc.date"))
    if published:
        published = published.replace("/", "-").strip()

    abstract = first(("name", "dc.Description"), ("name", "dc.description"), ("name", "description"), ("property", "og:description"))
    journal = first(("name", "citation_journal_title"), ("name", "prism.publicationName"))
    volume = first(("name", "citation_volume"), ("name", "prism.volume"))
    issue = first(("name", "citation_issue"), ("name", "prism.number"))
    firstpage = first(("name", "citation_firstpage"),)
    lastpage  = first(("name", "citation_lastpage"),)
    pages = f"{firstpage}-{lastpage}" if firstpage and lastpage else (firstpage or None)
    year = first(("name", "citation_year"), ("name", "prism.publicationDate"))
    if not year and published:
        m = re.match(r"(\d{4})", published)
        year = m.group(1) if m else None
    pdf_url = first(("name", "citation_pdf_url"),)

    return {
        "identifier": url,
        "title": title,
        "authors": ", ".join(authors) if authors else "Unknown",
        "published": published or "Unknown",
    }

# ---------------------------
# Nature (HTML meta tags)
# ---------------------------

def fetch_nature_metadata(article_url: str, timeout: int = 20) -> dict:
    """Fetch metadata from Nature article page."""
    url = article_url.strip()
    resp = requests.get(url, headers=_headers(), timeout=timeout)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch page ({resp.status_code}) for {url}")

    soup = BeautifulSoup(resp.text, "html.parser")

    def get_all(name=None, prop=None):
        if name:
            return [m.get("content", "").strip() for m in soup.find_all("meta", attrs={"name": name}) if m.get("content")]
        if prop:
            return [m.get("content", "").strip() for m in soup.find_all("meta", attrs={"property": prop}) if m.get("content")]
        return []

    def first(*cands):
        for kind, val in cands:
            vals = get_all(name=val if kind == "name" else None, prop=val if kind == "property" else None)
            if vals:
                return vals[0]
        return None

    title = first(("name", "citation_title"), ("property", "og:title"), ("property", "twitter:title"), ("name", "dc.Title"), ("name", "dc.title"))
    if not title:
        # Fallback to HTML title tag
        title_tag = soup.find("title")
        if title_tag:
            title_text = title_tag.get_text(strip=True)
            if title_text:
                title = title_text
                # Clean up title if it contains extra info
                if "|" in title:
                    title = title.split("|")[0].strip()
                if " | Nature" in title:
                    title = title.replace(" | Nature", "").strip()
        if not title:
            raise Exception("Failed to parse title from Nature page.")

    authors = get_all(name="citation_author") or get_all(name="dc.Creator") or get_all(name="dc.creator")
    if not authors:
        # Try alternative meta tag patterns
        authors = get_all(prop="article:author") or get_all(name="author")

    doi = first(("name", "citation_doi"), ("name", "dc.Identifier"), ("name", "dc.identifier")) or first(("name", "prism.doi"),)
    if doi and doi.lower().startswith("http"):
        m = re.search(r"(10\.\d{4,9}/\S+)", doi)
        doi = m.group(1) if m else doi

    published = first(("name", "citation_publication_date"), ("name", "prism.publicationDate"), ("name", "dc.Date"), ("name", "dc.date"))
    if published:
        published = published.replace("/", "-").strip()
        # Extract year if full date format
        if len(published) >= 4:
            published = published[:10] if len(published) > 10 else published

    return {
        "identifier": url,
        "title": title,
        "authors": ", ".join(authors) if authors else "Unknown",
        "published": published or "Unknown",
    }

# ---------------------------
# OpenReview (HTML meta tags)
# ---------------------------

def fetch_openreview_metadata(article_url: str, timeout: int = 20) -> dict:
    """Fetch metadata from OpenReview page."""
    # Normalize PDF URLs to HTML forum URLs for parsing
    original_url = article_url.strip()
    fetch_url = original_url
    if "/pdf?id=" in fetch_url:
        fetch_url = fetch_url.replace("/pdf?id=", "/forum?id=")
    elif fetch_url.endswith(".pdf"):
        # Handle /pdf/ID.pdf format
        fetch_url = fetch_url.replace("/pdf/", "/forum/").replace(".pdf", "")
    
    resp = requests.get(fetch_url, headers=_headers(), timeout=timeout)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch metadata for {fetch_url}")

    soup = BeautifulSoup(resp.text, "html.parser")

    def _first(*cands):
        for kind, val in cands:
            if kind == "name":
                m = soup.find("meta", attrs={"name": val})
            elif kind == "property":
                m = soup.find("meta", attrs={"property": val})
            else:
                m = soup.find(val[0], attrs={val[1]: val[2]}) if len(val) == 3 else None
            if m and m.get("content"):
                return m["content"].strip()
        return None

    # Try multiple strategies to find the title
    title = _first(
        ("name", "citation_title"),
        ("property", "og:title"),
        ("property", "twitter:title"),
    )
    
    # Fallback to HTML title tag
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            title_text = title_tag.get_text(strip=True)
            if title_text:
                title = title_text
                # Clean up title if it contains extra info
                if "|" in title:
                    title = title.split("|")[0].strip()
                if " - OpenReview" in title:
                    title = title.replace(" - OpenReview", "").strip()
    
    # Fallback to h1 tag
    if not title:
        h1_tag = soup.find("h1")
        if h1_tag:
            title_text = h1_tag.get_text(separator=" ", strip=True)
            if title_text and len(title_text) > 10:
                title = title_text
    
    # Fallback to JSON-LD structured data
    if not title:
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                script_content = script.string or script.get_text(strip=True)
                if not script_content:
                    continue
                data = json.loads(script_content)
                if isinstance(data, dict):
                    if "headline" in data:
                        title = data["headline"]
                    elif "name" in data:
                        title = data["name"]
                elif isinstance(data, list) and len(data) > 0:
                    item = data[0]
                    if isinstance(item, dict):
                        if "headline" in item:
                            title = item["headline"]
                        elif "name" in item:
                            title = item["name"]
                if title:
                    break
            except (json.JSONDecodeError, AttributeError, TypeError):
                continue
    
    if not title:
        raise Exception(f"Failed to parse title from OpenReview page {fetch_url}")

    # Extract authors
    authors = []
    # Try citation_author meta tags
    for m in soup.find_all("meta", attrs={"name": "citation_author"}):
        if m.get("content"):
            authors.append(m["content"].strip())
    
    # Fallback: try to find authors in the page structure
    if not authors:
        # Common OpenReview author patterns
        author_spans = soup.find_all(["span", "div"], class_=re.compile("note.*author|author.*name", re.I))
        for span in author_spans:
            author_text = span.get_text(separator=" ", strip=True)
            if author_text and len(author_text) > 2:
                authors.append(author_text)
        
        # Try to parse from JSON-LD
        if not authors:
            for script in soup.find_all("script", type="application/ld+json"):
                try:
                    script_content = script.string or script.get_text(strip=True)
                    if not script_content:
                        continue
                    data = json.loads(script_content)
                    if isinstance(data, dict) and "author" in data:
                        auth_list = data["author"]
                        if isinstance(auth_list, list):
                            for auth in auth_list:
                                if isinstance(auth, dict):
                                    name = auth.get("name") or (auth.get("givenName", "") + " " + auth.get("familyName", "")).strip()
                                    if name:
                                        authors.append(name)
                                elif isinstance(auth, str):
                                    authors.append(auth)
                    if authors:
                        break
                except (json.JSONDecodeError, AttributeError, TypeError):
                    continue

    # Extract published date
    published = _first(("name", "citation_publication_date"), ("name", "dc.date"))
    if published:
        published = published.split("T")[0]

    return {
        "identifier": original_url,
        "title": title,
        "authors": ", ".join(authors) if authors else "Unknown",
        "published": published or "Unknown",
    }

# ---------------------------
# Crossref (generic DOI fallback)
# ---------------------------

def fetch_crossref_by_doi(doi: str, timeout: int = 20) -> dict:
    """
    Generic DOI lookup via Crossref (works for most publishers).
    """
    api = f"https://api.crossref.org/works/{doi}"
    r = requests.get(api, headers=_headers(), timeout=timeout)
    if r.status_code != 200:
        raise Exception(f"Crossref lookup failed for DOI {doi} (status {r.status_code}).")
    data = r.json()["message"]

    title = (data.get("title") or ["Unknown"])[0]
    authors = []
    for a in data.get("author", []) or []:
        given = a.get("given", "")
        family = a.get("family", "")
        nm = (given + " " + family).strip() or a.get("name", "")
        if nm:
            authors.append(nm)
    container = (data.get("container-title") or [None])[0]
    year = None
    for key in ["issued", "published-print", "published-online"]:
        part = data.get(key, {}).get("date-parts", [[]])
        if part and part[0]:
            year = str(part[0][0])
            break

    pages = None
    if data.get("page"):
        pages = data["page"]
    volume = data.get("volume")
    issue = data.get("issue")
    url = data.get("URL")
    abstract = data.get("abstract")
    # Crossref abstracts may be JATS XML; leave as-is or strip tags upstream.

    return {
        "identifier": doi,
        "title": title,
        "authors": ", ".join(authors) if authors else "Unknown",
        "published": year or "Unknown",
    }

# ---------------------------
# Router
# ---------------------------

def fetch_paper_metadata(identifier: str, timeout: int = 20) -> dict:
    """
    Generalized metadata fetcher.
    Accepts:
      - arXiv ID/URL (e.g., '2401.01234', 'arXiv:2401.01234v2', 'https://arxiv.org/abs/2401.01234')
      - ChemRxiv URL
      - ACS DOI or URL
      - Nature URL
      - OpenReview URL
      - Any DOI (falls back to Crossref)
    """
    s = identifier.strip()

    # arXiv
    if _is_arxiv_id_or_url(s):
        return fetch_arxiv_metadata(s, timeout=timeout)

    # ChemRxiv
    if _is_chemrxiv_url(s):
        return fetch_chemrxiv_metadata(s, timeout=timeout)

    # OpenReview
    if _is_openreview_url(s):
        return fetch_openreview_metadata(s, timeout=timeout)

    # Nature - try Nature first, but fall back to Crossref if we can extract a DOI
    if _is_nature_url(s):
        try:
            return fetch_nature_metadata(s, timeout=timeout)
        except Exception as e:
            # If Nature fetch fails, try Crossref as fallback if we can extract a DOI
            doi = _extract_doi(s)
            if doi:
                print(f"Warning: Nature fetch failed ({e}), falling back to Crossref for DOI {doi}", file=sys.stderr)
                return fetch_crossref_by_doi(doi, timeout=timeout)
            raise

    # ACS - try ACS first, but fall back to Crossref if ACS blocks us (403)
    if _is_acs_url(s):
        try:
            return fetch_acs_metadata(s, timeout=timeout)
        except Exception as e:
            # If ACS blocks us (e.g., 403), try Crossref as fallback if we can extract a DOI
            doi = _extract_doi(s)
            if doi:
                print(f"Warning: ACS fetch failed ({e}), falling back to Crossref for DOI {doi}", file=sys.stderr)
                return fetch_crossref_by_doi(doi, timeout=timeout)
            raise

    # DOI (generic) — try ACS first if DOI belongs to ACS, else Crossref
    doi = _extract_doi(s)
    if doi:
        # If it looks like an ACS DOI (prefix patterns vary, but we can attempt ACS scrape first)
        try:
            return fetch_acs_metadata(doi, timeout=timeout)
        except Exception as e:
            # Not ACS or ACS blocked; use Crossref as fallback
            print(f"Warning: ACS fetch failed ({e}), falling back to Crossref for DOI {doi}", file=sys.stderr)
            return fetch_crossref_by_doi(doi, timeout=timeout)

    raise ValueError("Identifier not recognized as arXiv ID/URL, ChemRxiv URL, OpenReview URL, Nature URL, ACS URL/DOI, or generic DOI.")


def smart_title_case(text):
    words = text.split()  # Split the string into words
    capitalized_words = [
        word if word[:1].isupper() else word.capitalize() for word in words
    ]
    return " ".join(capitalized_words)  # Join the processed words back


def normalize_tags(tags):
    """Normalize tags by capitalizing the first letter of each word."""
    return [smart_title_case(tag) for tag in tags]


def update_papers_file(identifier, tags, partition, notes=""):
    """Update the _papers.yml file."""
    papers_file = f"_data/papers_{partition}.yml"

    # Load existing papers
    if os.path.exists(papers_file):
        with open(papers_file, "r") as file:
            papers = yaml.safe_load(file) or []
    else:
        papers = []

    # Check if identifier already exists (handle both "identifier" and "arxiv_id" for backwards compatibility)
    for paper in papers:
        paper_id = paper.get("identifier") or paper.get("arxiv_id")
        if paper_id == identifier:
            print(f"Paper with ID {identifier} already exists:")
            print(f"  Title: {paper.get('title', 'N/A')}")
            print(f"  Authors: {paper.get('authors', 'N/A')}")
            print(f"  Published: {paper.get('published', 'N/A')}")
            print(f"  Notes: {paper.get('notes', '')}")
            print(f"  Tags: {', '.join(paper.get('tags', []))}")

            override = input("Would you like to override it? (y/n): ").strip().lower()
            if override != "y":
                print("Operation aborted. No changes were made.")
                sys.exit(0)
            else:
                papers.remove(paper)
                break

    # Fetch metadata
    metadata = fetch_paper_metadata(identifier, timeout=20)
    metadata["identifier"] = identifier
    metadata["notes"] = notes
    metadata["tags"] = normalize_tags(tags)

    # Append to papers list
    papers.append(metadata)

    # Save updated file
    with open(papers_file, "w") as file:
        yaml.dump(papers, file, sort_keys=False)

    return metadata


def update_tag_colors(tags):
    """Update the tag_colors.yml file."""
    colors_file = "_data/tag_colors.yml"

    # Load existing tag colors
    if os.path.exists(colors_file):
        with open(colors_file, "r") as file:
            tag_colors = yaml.safe_load(file) or {}
    else:
        tag_colors = {}

    # Assign random colors to new tags
    for tag in tags:
        if tag not in tag_colors:
            tag_colors[tag] = f"#{random.randint(0, 0xFFFFFF):06x}"

    # Save updated file
    with open(colors_file, "w") as file:
        yaml.dump(tag_colors, file)

    return tag_colors


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <identifier> <partition> [notes] [tags]")
        sys.exit(1)

    identifier = sys.argv[1]
    partition = sys.argv[2]
    tags = sys.argv[3:]

    # Normalize tags
    tags = normalize_tags(tags)

    # Update papers and tag colors
    metadata = update_papers_file(identifier, tags, partition)
    update_tag_colors(tags)

    # Success message
    url = metadata.get('url') or metadata.get('identifier', 'N/A')
    notes = metadata.get('notes', '')
    print(
        f"Successfully added/updated paper:\n  Title: {metadata['title']}\n  Authors: {metadata['authors']}\n  Published: {metadata['published']}\n  URL: {url}\n  Notes: {notes}\n  Tags: {', '.join(tags)}"
    )


if __name__ == "__main__":
    main()
