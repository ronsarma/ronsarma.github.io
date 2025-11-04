$(document).ready(function () {
  // add toggle functionality to abstract, award and bibtex buttons
  $("a.abstract").click(function () {
    $(this).parent().parent().find(".abstract.hidden").toggleClass("open");
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.award").click(function () {
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".award.hidden").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden.open").toggleClass("open");
  });
  $("a.bibtex").click(function () {
    $(this).parent().parent().find(".abstract.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".award.hidden.open").toggleClass("open");
    $(this).parent().parent().find(".bibtex.hidden").toggleClass("open");
  });
  $("a").removeClass("waves-effect waves-light");

  // bootstrap-toc
  if ($("#toc-sidebar").length) {
    // remove related publications years from the TOC
    $(".publications h2").each(function () {
      $(this).attr("data-toc-skip", "");
    });
    var navSelector = "#toc-sidebar";
    var $myNav = $(navSelector);
    
    // Calculate scroll offset for fixed navbar
    var scrollOffset = 0;
    if ($("#navbar").hasClass("fixed-top")) {
      scrollOffset = $("#navbar").outerHeight(true) || 60; // Default to 60px if height can't be determined
    }
    
    // Initialize bootstrap-toc (by default it includes top level + 1 level below)
    Toc.init($myNav);
    
    // Manually add specific deeper heading levels (h5) as subsections
    // Bootstrap-toc only includes 2 levels by default, so we need to add h5 headings
    function addDeepHeadings() {
      var $tocNav = $myNav.find("ul.nav").first();
      if ($tocNav.length === 0) return;
      
      // Get only h5 headings in order within the main content
      var $container = $(".container");
      var $allHeadings = $container.find("h5").not("[data-toc-skip]");
      
      // Create a map of heading IDs to TOC items for quick lookup
      var idToTocItem = {};
      $tocNav.find("a.nav-link").each(function() {
        var href = $(this).attr("href");
        if (href && href.indexOf("#") === 0) {
          idToTocItem[href.substring(1)] = $(this).closest("li");
        }
      });
      
      // Process each heading
      $allHeadings.each(function() {
        var $heading = $(this);
        var headingLevel = parseInt(this.tagName.charAt(1));
        var headingId = this.id;
        var headingText = $heading.data("toc-text") || $heading.text().trim();
        
        // Ensure heading has an ID
        if (!headingId) {
          headingId = "toc-" + headingText.toLowerCase()
            .replace(/[^\w\s-]/g, '')
            .replace(/\s+/g, '-')
            .replace(/-+/g, '-')
            .substring(0, 50);
          // Make sure ID is unique
          var baseId = headingId;
          var counter = 0;
          while (document.getElementById(headingId)) {
            headingId = baseId + "-" + (++counter);
          }
          this.id = headingId;
        }
        
        // Check if already in TOC
        if (idToTocItem[headingId]) return;
        
        // Find the appropriate parent heading (closest higher-level heading before this one)
        var $parentHeading = null;
        for (var level = headingLevel - 1; level >= 2; level--) {
          $heading.prevAll("h" + level).each(function() {
            if (!$parentHeading) {
              $parentHeading = $(this);
              return false; // break
            }
          });
          if ($parentHeading) break;
        }
        
        // Find the parent TOC item
        var $parentNavItem = null;
        if ($parentHeading && $parentHeading.length && $parentHeading[0].id) {
          $parentNavItem = idToTocItem[$parentHeading[0].id];
        }
        
        // If no parent, attach to the last top-level item, or create new top-level
        if (!$parentNavItem || !$parentNavItem.length) {
          $parentNavItem = $tocNav.find("> li").last();
          if (!$parentNavItem.length) {
            $parentNavItem = null; // Will create top-level item
          }
        }
        
        // Create the nav item
        var $navItem = $('<li><a class="nav-link" href="#' + headingId + '">' + 
                         headingText + '</a></li>');
        
        if ($parentNavItem && $parentNavItem.length) {
          // Add as child
          var $childList = $parentNavItem.find("> ul.nav").first();
          if (!$childList.length) {
            $childList = $('<ul class="nav"></ul>');
            $parentNavItem.append($childList);
          }
          $childList.append($navItem);
        } else {
          // Add as top-level item
          $tocNav.append($navItem);
        }
        
        // Update map
        idToTocItem[headingId] = $navItem;
      });
    }
    
    // Add deep headings after a short delay to ensure bootstrap-toc has finished
    setTimeout(addDeepHeadings, 100);
    
    $("body").scrollspy({
      target: navSelector,
      offset: scrollOffset + 10 // Add 10px buffer for better visibility
    });
    
    // Add smooth scrolling and proper anchor navigation using event delegation
    // This ensures it works even if TOC is generated dynamically
    $(document).on("click", navSelector + " a", function(e) {
      var href = $(this).attr("href");
      if (href && href.indexOf("#") !== -1) {
        var targetId = href.substring(href.indexOf("#"));
        var $target = $(targetId);
        if ($target.length) {
          e.preventDefault();
          var targetOffset = $target.offset().top - scrollOffset;
          $("html, body").animate({
            scrollTop: targetOffset
          }, 400, "swing", function() {
            // Update URL hash without scrolling again
            if (history.pushState) {
              history.pushState(null, null, targetId);
            } else {
              window.location.hash = targetId;
            }
          });
        }
      }
    });
  }

  // add css to jupyter notebooks
  const cssLink = document.createElement("link");
  cssLink.href = "../css/jupyter.css";
  cssLink.rel = "stylesheet";
  cssLink.type = "text/css";

  let jupyterTheme = determineComputedTheme();

  $(".jupyter-notebook-iframe-container iframe").each(function () {
    $(this).contents().find("head").append(cssLink);

    if (jupyterTheme == "dark") {
      $(this).bind("load", function () {
        $(this).contents().find("body").attr({
          "data-jp-theme-light": "false",
          "data-jp-theme-name": "JupyterLab Dark",
        });
      });
    }
  });

  // trigger popovers
  $('[data-toggle="popover"]').popover({
    trigger: "hover",
  });
});
