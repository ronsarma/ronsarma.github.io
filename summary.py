import argparse
import re
from arxiv2bib import arxiv2bib
from datetime import date
import sys
import os

# Import fetch_paper_metadata from reading_list.py
# Assume reading_list.py is in the same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reading_list import fetch_paper_metadata, _is_arxiv_id_or_url, _normalize_arxiv_id, _extract_doi

def retrieve_arxiv_bib(id):
    return arxiv2bib([id])[0]

def clean_title(title):
    title = title.strip()
    title = title.replace("\n", "")
    title = re.sub(" +", " ", title)
    return title

# title can contain spaces, caps
def filename(title):
    today = date.today()
    title = title.lower()
    title = title.replace(" ", "-")
    title = title.replace(",", "")
    title = title.replace(":", "")
    title = title.strip()
    title = re.sub("-+", "-", title)
    title = ''.join(e for e in title if e.isalnum() or e == "-")
    print("Filename", title)
    return f"_summaries/{today}-{title}.markdown"

def eprint_without_version(eprint):
    return re.sub("v\d+", "", eprint)

def generate_citation_key(identifier, metadata):
    """Generate a BibTeX citation key from identifier and metadata."""
    # For arXiv papers, use the arXiv ID as the key
    if _is_arxiv_id_or_url(identifier):
        arxiv_id = _normalize_arxiv_id(identifier)
        # Keep version if present, otherwise use base ID
        if 'v' in arxiv_id:
            return arxiv_id
        else:
            return arxiv_id
    
    # For DOI-based papers, create key from DOI
    doi = _extract_doi(identifier)
    if doi:
        # Use DOI with slashes replaced by underscores
        key = doi.replace("/", "_").replace(".", "_")
        # Remove http/https prefixes if present
        key = re.sub(r'^https?://', '', key)
        key = re.sub(r'[^a-zA-Z0-9_]', '_', key)
        return key[:50]  # Limit length
    
    # For other sources, create key from first author last name and year
    authors = metadata.get('authors', 'Unknown')
    published = metadata.get('published', 'Unknown')
    
    # Extract year from published date
    year = 'Unknown'
    if published and published != 'Unknown':
        year_match = re.search(r'(\d{4})', published)
        if year_match:
            year = year_match.group(1)
    
    # Extract first author's last name
    first_author = authors.split(',')[0].strip() if authors else 'Unknown'
    if first_author and first_author != 'Unknown':
        # Try to get last name (assume "First Last" or "Last, First" format)
        parts = first_author.split()
        if len(parts) > 0:
            last_name = parts[-1] if ',' not in first_author else parts[0].rstrip(',')
            last_name = re.sub(r'[^a-zA-Z]', '', last_name)
            # Create key from last name, year, and first word of title
            title = metadata.get('title', '')[:20]
            title_slug = re.sub(r'[^a-zA-Z0-9]', '', title.split()[0] if title.split() else '')
            return f"{last_name}{year}{title_slug}"[:50]
    
    # Fallback: create key from identifier
    key = re.sub(r'[^a-zA-Z0-9]', '_', identifier)
    return key[:50]

def generate_bibtex_from_metadata(metadata, citation_key, identifier):
    """Generate BibTeX entry from metadata."""
    title = metadata.get('title', 'Unknown')
    authors = metadata.get('authors', 'Unknown')
    published = metadata.get('published', 'Unknown')
    
    # Determine entry type - default to @article, use @inproceedings for conference papers
    entry_type = "@article"
    
    # Extract year from published date
    year = 'Unknown'
    if published and published != 'Unknown':
        year_match = re.search(r'(\d{4})', published)
        if year_match:
            year = year_match.group(1)
    
    bibtex = f"@{entry_type}{{{citation_key},\n"
    bibtex += f"  title         = {{{title}}},\n"
    bibtex += f"  author        = {{{authors}}},\n"
    
    # Add arXiv-specific fields if it's an arXiv paper
    if _is_arxiv_id_or_url(identifier):
        arxiv_id = _normalize_arxiv_id(identifier)
        bibtex += f"  eprint        = {{{arxiv_id}}},\n"
        bibtex += f"  archiveprefix = {{arXiv}},\n"
        # Try to get primary class from arxiv2bib if available
        try:
            bib = retrieve_arxiv_bib(arxiv_id)
            if hasattr(bib, 'primary_class') and bib.primary_class:
                bibtex += f"  primaryclass  = {{{bib.primary_class}}},\n"
        except:
            pass
        bibtex += f"  url           = {{http://arxiv.org/abs/{eprint_without_version(arxiv_id)}}},\n"
        bibtex += f"  year          = {{{year}}},\n"
        bibtex += f"  EprintNoVer   = {{{eprint_without_version(arxiv_id)}}}\n"
    else:
        # For non-arXiv papers, add DOI if available
        doi = _extract_doi(identifier)
        if doi:
            bibtex += f"  doi           = {{{doi}}},\n"
            bibtex += f"  url           = {{https://doi.org/{doi}}},\n"
        else:
            # Use identifier as URL if it looks like a URL
            if identifier.startswith('http'):
                bibtex += f"  url           = {{{identifier}}},\n"
        
        bibtex += f"  year          = {{{year}}},\n"
        # Add published date if we have full date
        if published and published != 'Unknown' and len(published) > 4:
            bibtex += f"  date          = {{{published}}},\n"
    
    bibtex += "}"
    
    return bibtex

def template(title, bib_id):
    return \
f"""---
layout: summary
title: "{title}"
giscus_comments: true
bib_id: {bib_id}
---

### Three Important Things

#### 1. Foo

#### 2. Bar

#### 3. Baz

### Most Glaring Deficiency

### Conclusions for Future Work
"""

def create_summary_template(title, bib_id):
    filepath = filename(title)

    with open(filepath, "w") as f:
        f.write(template(title, bib_id))

    print(f"New summary template created at {filepath}")

def update_summary_bib(bibtex, citation_key):
    """Update summaries.bib with the BibTeX entry."""
    with open("_bibliography/summaries.bib", "a") as f:
        f.write("\n\n")
        f.write(bibtex)
    
    print("Updated _bibliography/summaries.bib with")
    print(bibtex)

def main():
    parser = argparse.ArgumentParser(
        description='Create summary template from paper identifier (arXiv ID, DOI, URL, etc.)'
    )
    parser.add_argument('--identifier', type=str,
                        help='Paper identifier (arXiv ID, DOI, URL, etc.)', required=False)
    parser.add_argument('--arxiv_id', type=str,
                        help='arXiv article ID (deprecated, use --identifier)', required=False)
    parser.add_argument('--title', required=False,
                        help='Manual title override (requires --bib-id)')
    parser.add_argument('--bib-id', required=False,
                        help='Manual BibTeX citation key (requires --title)')
    args = parser.parse_args()

    if args.title:
        # Manual mode: just create template with provided title and bib_id
        if not args.bib_id:
            print("Error: --bib-id is required when using --title")
            sys.exit(1)
        title = args.title
        bib_id = args.bib_id
        create_summary_template(title, bib_id)
    else:
        # Automatic mode: fetch metadata and generate BibTeX
        identifier = args.identifier or args.arxiv_id
        if not identifier:
            print("Error: --identifier (or --arxiv_id) is required")
            sys.exit(1)
        
        # Fetch metadata using reading_list.py
        print(f"Fetching metadata for: {identifier}")
        try:
            metadata = fetch_paper_metadata(identifier, timeout=20)
        except Exception as e:
            print(f"Error fetching metadata: {e}")
            sys.exit(1)
        
        title = clean_title(metadata['title'])
        print(f"Title: {title}")
        print(f"Authors: {metadata.get('authors', 'Unknown')}")
        print(f"Published: {metadata.get('published', 'Unknown')}")
        
        # Generate citation key
        citation_key = generate_citation_key(identifier, metadata)
        print(f"Citation key: {citation_key}")
        
        # Generate BibTeX
        # For arXiv papers, try to use arxiv2bib for better BibTeX (including abstract, etc.)
        if _is_arxiv_id_or_url(identifier):
            try:
                arxiv_id = _normalize_arxiv_id(identifier)
                bib = retrieve_arxiv_bib(arxiv_id)
                bibtex = bib.bibtex()
                # Add EprintNoVer field
                bibtex = bibtex[:-2]
                bibtex += f",\n  EprintNoVer   = {{{eprint_without_version(arxiv_id)}}}\n}}"
                citation_key = bib.id  # Use the citation key from arxiv2bib
            except Exception as e:
                print(f"Warning: Could not use arxiv2bib ({e}), generating BibTeX from metadata")
                bibtex = generate_bibtex_from_metadata(metadata, citation_key, identifier)
        else:
            bibtex = generate_bibtex_from_metadata(metadata, citation_key, identifier)
        
        # Create summary template
        create_summary_template(title, citation_key)
        
        # Update BibTeX file
        update_summary_bib(bibtex, citation_key)


if __name__ == "__main__":
    main()