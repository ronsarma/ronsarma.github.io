module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  // Safelist CSS custom properties (variables) and important selectors
  safelist: {
    // Preserve all CSS custom properties and any rules containing them
    greedy: [
      /--global-/,
      /--fa/,
      /var\(--/,
    ],
    // Preserve attribute selectors for theme switching
    standard: [
      /^html\[data-theme/,
      /^:root/,
      '#light-toggle-system',
      '#light-toggle-dark',
      '#light-toggle-light',
      '#back-to-top',
      '.only-light',
      '.only-dark',
      '[data-theme]',
      '[data-theme-setting]',
    ],
    // Deep selectors that might be used dynamically
    deep: [
      /\[data-theme/,
      /^:root/,
      /^html\[/,
    ],
  },
};
