---
layout: page
permalink: /papers/
title: Papers
description: >
    This section is about my interactions with research papers - most often they are a lot to read and parse through, but sometimes they are totally worth it. The first part, summaries, is where I have my own inter-pretations and takes on various papers that I have read. The second part, reading list, is a curated list of papers that I want to read (someday).
nav: true
nav_order: 3
toc:
    sidebar: left
---

## Summaries

I share summaries and opinions of papers that I've read in detail, across multiple disciplines. Most of it will concise key points that I find interesting, and perhaps some personal takes.

This serves to both as a platform to intiate academic discussions and as a catalog for my own reading. Feel free to connect with me and start a discussion on any statement that interests you, or even better, correct or teach me when I am wrong. 

This format is inspired from <a href="https://fanpu.io/">Fan Pu's</a> website.

<div style="text-align: center; padding: 3rem 2rem; margin: 2rem 0; border: 2px dashed rgba(128, 128, 128, 0.3); border-radius: 12px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);">
  <h3 style="margin: 0.5rem 0; font-weight: 300; letter-spacing: 2px; color: #666;">COMING SOON</h3>
  <p style="margin: 0.5rem 0 0 0; color: #888; font-style: italic; font-size: 0.95rem;">Summaries are in the works...</p>
</div>

{% include scripts/mathjax_macros.html %}

---
<!-- 
<ol>
    {% for summary in site.summaries reversed %}
    <li>
        <a href="{{ summary.url | relative_url }}">
            ({{ summary.date | date: '%b %-d, %Y' }})
            {{ summary.title }}
        </a>
    </li>
    {% endfor %}
</ol>

---
<br> -->
<br>
## Reading List

##### Atomistic Models
<div class="mb-3">
  <span id="filter-badge" class="badge" style="display:none;"></span>
</div>

<ul class="card-text font-weight-light list-group list-group-flush" id="papers-list">
  {% assign papers = site.data.papers_MLIP | reverse %}
  {% for paper in papers %}
    <li class="list-group-item" data-tags="{{ paper.tags | join: ' ' }}">
      <div class="row">
        <div class="col">
          <h6 class="title font-weight-bold ml-1 ml-md-4">
            {% if paper.identifier contains 'http://' or paper.identifier contains 'https://' %}
              {{ forloop.index }}. <a href="{{ paper.identifier }}">{{ paper.title }}</a>
            {% else %}
              {{ forloop.index }}. <a href="https://arxiv.org/abs/{{ paper.identifier }}">{{ paper.title }}</a>
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem; font-style: italic; color: #888">
            {% assign authors_list = paper.authors | split: ',' %}
            {% if authors_list.size > 7 %}
              {{ authors_list | slice: 0, 7 | join: ', ' }} et al.
            {% else %}
              {{ authors_list | join: ', ' }}
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem">
            {{ paper.notes }}
          </h6>

          {% if paper.tags %}
            <div class="ml-1 ml-md-4">
              {% assign sorted_tags = paper.tags | sort %}
              {% for tag in sorted_tags %}
                {% assign bgColor = site.data.tag_colors[tag] | default: "#ccc" %}
                <a href="#{{ tag | downcase | replace: ' ', '-' }}"
                   class="badge"
                   data-color="{{ bgColor }}"
                   style="background-color:{{ bgColor }}">
                  {{ tag }}
                </a>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <div class="col-auto text-right">
          {% if paper.published %}
            {% assign date = paper.published %}
            <span class="text-muted" style="font-size: 0.85rem;">
              {{ date }}
            </span>
          {% endif %}
        </div>
      </div>
    </li>
  {% endfor %}
</ul>

<br>

##### Chemistry
<div class="mb-3">
  <span id="filter-badge" class="badge" style="display:none;"></span>
</div>

<ul class="card-text font-weight-light list-group list-group-flush" id="papers-list">
  {% assign papers = site.data.papers_chem | reverse %}
  {% for paper in papers %}
    <li class="list-group-item" data-tags="{{ paper.tags | join: ' ' }}">
      <div class="row">
        <div class="col">
          <h6 class="title font-weight-bold ml-1 ml-md-4">
            {% if paper.identifier contains 'http://' or paper.identifier contains 'https://' %}
              {{ forloop.index }}. <a href="{{ paper.identifier }}">{{ paper.title }}</a>
            {% else %}
              {{ forloop.index }}. <a href="https://arxiv.org/abs/{{ paper.identifier }}">{{ paper.title }}</a>
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem; font-style: italic; color: #888">
            {% assign authors_list = paper.authors | split: ',' %}
            {% if authors_list.size > 7 %}
              {{ authors_list | slice: 0, 7 | join: ', ' }} et al.
            {% else %}
              {{ authors_list | join: ', ' }}
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem">
            {{ paper.notes }}
          </h6>

          {% if paper.tags %}
            <div class="ml-1 ml-md-4">
              {% assign sorted_tags = paper.tags | sort %}
              {% for tag in sorted_tags %}
                {% assign bgColor = site.data.tag_colors[tag] | default: "#ccc" %}
                <a href="#{{ tag | downcase | replace: ' ', '-' }}"
                   class="badge"
                   data-color="{{ bgColor }}"
                   style="background-color:{{ bgColor }}">
                  {{ tag }}
                </a>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <div class="col-auto text-right">
          {% if paper.published %}
            {% assign date = paper.published %}
            <span class="text-muted" style="font-size: 0.85rem;">
              {{ date }}
            </span>
          {% endif %}
        </div>
      </div>
    </li>
  {% endfor %}
</ul>
<br>

##### Deep Learning
<div class="mb-3">
  <span id="filter-badge" class="badge" style="display:none;"></span>
</div>

<ul class="card-text font-weight-light list-group list-group-flush" id="papers-list">
  {% assign papers = site.data.papers_Deep-Learning | reverse %}
  {% for paper in papers %}
    <li class="list-group-item" data-tags="{{ paper.tags | join: ' ' }}">
      <div class="row">
        <div class="col">
          <h6 class="title font-weight-bold ml-1 ml-md-4">
            {% if paper.identifier contains 'http://' or paper.identifier contains 'https://' %}
              {{ forloop.index }}. <a href="{{ paper.identifier }}">{{ paper.title }}</a>
            {% else %}
              {{ forloop.index }}. <a href="https://arxiv.org/abs/{{ paper.identifier }}">{{ paper.title }}</a>
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem; font-style: italic; color: #888">
            {% assign authors_list = paper.authors | split: ',' %}
            {% if authors_list.size > 7 %}
              {{ authors_list | slice: 0, 7 | join: ', ' }} et al.
            {% else %}
              {{ authors_list | join: ', ' }}
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem">
            {{ paper.notes }}
          </h6>

          {% if paper.tags %}
            <div class="ml-1 ml-md-4">
              {% assign sorted_tags = paper.tags | sort %}
              {% for tag in sorted_tags %}
                {% assign bgColor = site.data.tag_colors[tag] | default: "#ccc" %}
                <a href="#{{ tag | downcase | replace: ' ', '-' }}"
                   class="badge"
                   data-color="{{ bgColor }}"
                   style="background-color:{{ bgColor }}">
                  {{ tag }}
                </a>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <div class="col-auto text-right">
          {% if paper.published %}
            {% assign date = paper.published %}
            <span class="text-muted" style="font-size: 0.85rem;">
              {{ date }}
            </span>
          {% endif %}
        </div>
      </div>
    </li>
  {% endfor %}
</ul>
<br>

##### Generation and Exploration
<div class="mb-3">
  <span id="filter-badge" class="badge" style="display:none;"></span>
</div>

<ul class="card-text font-weight-light list-group list-group-flush" id="papers-list">
  {% assign papers = site.data.papers_generation | reverse %}
  {% for paper in papers %}
    <li class="list-group-item" data-tags="{{ paper.tags | join: ' ' }}">
      <div class="row">
        <div class="col">
          <h6 class="title font-weight-bold ml-1 ml-md-4">
            {% if paper.identifier contains 'http://' or paper.identifier contains 'https://' %}
              {{ forloop.index }}. <a href="{{ paper.identifier }}">{{ paper.title }}</a>
            {% else %}
              {{ forloop.index }}. <a href="https://arxiv.org/abs/{{ paper.identifier }}">{{ paper.title }}</a>
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem; font-style: italic; color: #888">
            {% assign authors_list = paper.authors | split: ',' %}
            {% if authors_list.size > 7 %}
              {{ authors_list | slice: 0, 7 | join: ', ' }} et al.
            {% else %}
              {{ authors_list | join: ', ' }}
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem">
            {{ paper.notes }}
          </h6>

          {% if paper.tags %}
            <div class="ml-1 ml-md-4">
              {% assign sorted_tags = paper.tags | sort %}
              {% for tag in sorted_tags %}
                {% assign bgColor = site.data.tag_colors[tag] | default: "#ccc" %}
                <a href="#{{ tag | downcase | replace: ' ', '-' }}"
                   class="badge"
                   data-color="{{ bgColor }}"
                   style="background-color:{{ bgColor }}">
                  {{ tag }}
                </a>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <div class="col-auto text-right">
          {% if paper.published %}
            {% assign date = paper.published %}
            <span class="text-muted" style="font-size: 0.85rem;">
              {{ date }}
            </span>
          {% endif %}
        </div>
      </div>
    </li>
  {% endfor %}
</ul>
<br>

##### Retrosynthesis and Solubility
<div class="mb-3">
  <span id="filter-badge" class="badge" style="display:none;"></span>
</div>

<ul class="card-text font-weight-light list-group list-group-flush" id="papers-list">
  {% assign papers = site.data.papers_rns | reverse %}
  {% for paper in papers %}
    <li class="list-group-item" data-tags="{{ paper.tags | join: ' ' }}">
      <div class="row">
        <div class="col">
          <h6 class="title font-weight-bold ml-1 ml-md-4">
            {% if paper.identifier contains 'http://' or paper.identifier contains 'https://' %}
              {{ forloop.index }}. <a href="{{ paper.identifier }}">{{ paper.title }}</a>
            {% else %}
              {{ forloop.index }}. <a href="https://arxiv.org/abs/{{ paper.identifier }}">{{ paper.title }}</a>
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem; font-style: italic; color: #888">
            {% assign authors_list = paper.authors | split: ',' %}
            {% if authors_list.size > 7 %}
              {{ authors_list | slice: 0, 7 | join: ', ' }} et al.
            {% else %}
              {{ authors_list | join: ', ' }}
            {% endif %}
          </h6>
          <h6 class="ml-1 ml-md-4" style="font-size: 0.95rem">
            {{ paper.notes }}
          </h6>

          {% if paper.tags %}
            <div class="ml-1 ml-md-4">
              {% assign sorted_tags = paper.tags | sort %}
              {% for tag in sorted_tags %}
                {% assign bgColor = site.data.tag_colors[tag] | default: "#ccc" %}
                <a href="#{{ tag | downcase | replace: ' ', '-' }}"
                   class="badge"
                   data-color="{{ bgColor }}"
                   style="background-color:{{ bgColor }}">
                  {{ tag }}
                </a>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <div class="col-auto text-right">
          {% if paper.published %}
            {% assign date = paper.published %}
            <span class="text-muted" style="font-size: 0.85rem;">
              {{ date }}
            </span>
          {% endif %}
        </div>
      </div>
    </li>
  {% endfor %}
</ul>

<script>
(function() {
  // Helper: returns '#000' or '#fff' depending on color brightness
  function getContrastColor(hexColor) {
    // Defensive check
    if (!hexColor || !/^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$/.test(hexColor)) {
      return '#000';
    }
    // Normalize short form #abc => #aabbcc
    if (hexColor.length === 4) {
      hexColor = '#' + hexColor[1] + hexColor[1] 
                     + hexColor[2] + hexColor[2] 
                     + hexColor[3] + hexColor[3];
    }
    // Extract r, g, b
    var r = parseInt(hexColor.substr(1, 2), 16);
    var g = parseInt(hexColor.substr(3, 2), 16);
    var b = parseInt(hexColor.substr(5, 2), 16);

    // Approximate luminance
    // (You can tweak the 128 threshold if needed)
    var luminance = 0.299*r + 0.587*g + 0.114*b;
    return (luminance >= 128) ? '#000' : '#fff';
  }

  // 1. Build a color map from normalized tag -> color
  var tagColors = {};
  var tagLookup = {};

  {% for tagName in site.data.tag_colors %}
    (function() {
      var originalText = "{{ tagName[0] }}"; // e.g. "Deep Learning"
      var normalizedTag = originalText.toLowerCase().replace(/\s+/g, '-'); // e.g. "deep-learning"
      var colorValue = "{{ tagName[1] }}";
      tagColors[normalizedTag] = colorValue;
      tagLookup[normalizedTag] = originalText;
    })();
  {% endfor %}

  // Fallback color
  function getTagColor(normalizedTag) {
    return tagColors[normalizedTag] || '#ccc';
  }

  // 2. Get all filter badges and papers lists (one for each section)
  var filterBadges = document.querySelectorAll('#filter-badge');
  var papersLists = document.querySelectorAll('#papers-list');
  var allBadges = document.querySelectorAll('a.badge');

  // Helper: Check if hash is a known tag (not a heading anchor)
  function isKnownTag(normalizedTag) {
    return normalizedTag && tagLookup.hasOwnProperty(normalizedTag);
  }

  // 3. Show/hide the filter badge with a clickable ×
  function updateFilterBadge(normalizedTag, filterBadge) {
    if (!filterBadge) return;
    if (normalizedTag) {
      var originalText = tagLookup[normalizedTag] || normalizedTag;
      var colorValue = getTagColor(normalizedTag);
      filterBadge.style.display = '';
      filterBadge.style.backgroundColor = colorValue;
      var contrast = getContrastColor(colorValue);
      filterBadge.style.setProperty('color', contrast, 'important');
      filterBadge.innerHTML = originalText
        + ' <span class="cancel-filter" style="cursor:pointer; margin-left:6px; color:inherit;">&times;</span>';
    } else {
      filterBadge.style.display = 'none';
      filterBadge.innerHTML = '';
    }
  }

  // 4. Filter items by the normalized tag for a specific papers list
  function filterByTag(normalizedTag, papersList) {
    if (!papersList) return;
    
    // Find the corresponding filter badge (sibling or in the same section)
    var filterBadge = papersList.previousElementSibling;
    if (filterBadge && filterBadge.id === 'filter-badge') {
      updateFilterBadge(normalizedTag, filterBadge);
    }

    var papersListItems = papersList.querySelectorAll('li');
    papersListItems.forEach(function(item) {
      var rawTags = item.getAttribute('data-tags') || "";
      var rawTagsLower = rawTags.toLowerCase();
      var rawTagsHyphenated = rawTagsLower.replace(/\s+/g, '-'); 
      var show = !normalizedTag || rawTagsHyphenated.includes(normalizedTag);
      item.style.display = show ? '' : 'none';
    });
  }

  // 5. Handle changes to the hash - only filter if it's a known tag
  window.addEventListener('hashchange', function() {
    var hashVal = window.location.hash.replace('#','').toLowerCase();
    // Only filter if it's a known tag, not a heading anchor
    if (isKnownTag(hashVal)) {
      papersLists.forEach(function(papersList) {
        filterByTag(hashVal, papersList);
      });
    } else {
      // Clear all filters if hash is not a tag
      papersLists.forEach(function(papersList) {
        filterByTag('', papersList);
      });
    }
  });

  // 6. Filter on page load if a hash is present (only if it's a known tag)
  var initialHash = window.location.hash.replace('#','').toLowerCase();
  if (isKnownTag(initialHash)) {
    papersLists.forEach(function(papersList) {
      filterByTag(initialHash, papersList);
    });
  } else {
    // Clear all filters on initial load if hash is not a tag
    papersLists.forEach(function(papersList) {
      filterByTag('', papersList);
    });
  }

  // 7. Clicking the cross resets the filter (using event delegation for multiple badges)
  document.addEventListener('click', function(e) {
    if (e.target.classList.contains('cancel-filter')) {
      window.location.hash = ''; // triggers hashchange
    }
  });

  // 8. Adjust text color for each inline badge
  allBadges.forEach(function(badge) {
  var rawColor = badge.getAttribute('data-color') || '#ccc';
  var contrast = getContrastColor(rawColor);
  // Force override with !important
  badge.style.setProperty('color', contrast, 'important');
});

})();
</script>