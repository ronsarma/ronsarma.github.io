// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-projects",
          title: "projects",
          description: "a growing collection of projects that I have worked on or am currently working on.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-papers",
          title: "papers",
          description: "This section is about my interactions with research papers - most often they are a lot to read and parse through, but sometimes they are totally worth it. The first part, summaries, is where I have my own interpretations and takes various papers that I have read. The second part, reading list, is a curated list of papers that I want to read (if I ever have the time).",
          section: "Navigation",
          handler: () => {
            window.location.href = "/papers/";
          },
        },{id: "nav-bookshelf",
          title: "bookshelf",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/books/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "post-a-post-with-image-galleries",
      
        title: "a post with image galleries",
      
      description: "this is what included image galleries could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/photo-gallery/";
        
      },
    },{id: "post-a-post-with-tabs",
      
        title: "a post with tabs",
      
      description: "this is what included tabs in a post could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/tabs/";
        
      },
    },{id: "post-a-post-with-typograms",
      
        title: "a post with typograms",
      
      description: "this is what included typograms code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/typograms/";
        
      },
    },{id: "post-a-post-that-can-be-cited",
      
        title: "a post that can be cited",
      
      description: "this is what a post that can be cited looks like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/post-citation/";
        
      },
    },{id: "post-a-post-with-pseudo-code",
      
        title: "a post with pseudo code",
      
      description: "this is what included pseudo code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/pseudocode/";
        
      },
    },{id: "post-a-post-with-code-diff",
      
        title: "a post with code diff",
      
      description: "this is how you can display code diffs",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/code-diff/";
        
      },
    },{id: "post-a-post-with-advanced-image-components",
      
        title: "a post with advanced image components",
      
      description: "this is what advanced image components could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/advanced-images/";
        
      },
    },{id: "post-a-post-with-vega-lite",
      
        title: "a post with vega lite",
      
      description: "this is what included vega lite code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/vega-lite/";
        
      },
    },{id: "post-a-post-with-geojson",
      
        title: "a post with geojson",
      
      description: "this is what included geojson code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/geojson-map/";
        
      },
    },{id: "post-a-post-with-echarts",
      
        title: "a post with echarts",
      
      description: "this is what included echarts code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/echarts/";
        
      },
    },{id: "post-a-post-with-chart-js",
      
        title: "a post with chart.js",
      
      description: "this is what included chart.js code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2024/chartjs/";
        
      },
    },{id: "post-a-post-with-tikzjax",
      
        title: "a post with TikZJax",
      
      description: "this is what included TikZ code could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/tikzjax/";
        
      },
    },{id: "post-a-post-with-bibliography",
      
        title: "a post with bibliography",
      
      description: "an example of a blog post with bibliography",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/post-bibliography/";
        
      },
    },{id: "post-a-post-with-jupyter-notebook",
      
        title: "a post with jupyter notebook",
      
      description: "an example of a blog post with jupyter notebook",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/jupyter-notebook/";
        
      },
    },{id: "post-a-post-with-custom-blockquotes",
      
        title: "a post with custom blockquotes",
      
      description: "an example of a blog post with custom blockquotes",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/custom-blockquotes/";
        
      },
    },{id: "post-a-post-with-table-of-contents-on-a-sidebar",
      
        title: "a post with table of contents on a sidebar",
      
      description: "an example of a blog post with table of contents on a sidebar",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/sidebar-table-of-contents/";
        
      },
    },{id: "post-a-post-with-audios",
      
        title: "a post with audios",
      
      description: "this is what included audios could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/audios/";
        
      },
    },{id: "post-a-post-with-videos",
      
        title: "a post with videos",
      
      description: "this is what included videos could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/videos/";
        
      },
    },{id: "post-displaying-beautiful-tables-with-bootstrap-tables",
      
        title: "displaying beautiful tables with Bootstrap Tables",
      
      description: "an example of how to use Bootstrap Tables",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/tables/";
        
      },
    },{id: "post-a-post-with-table-of-contents",
      
        title: "a post with table of contents",
      
      description: "an example of a blog post with table of contents",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2023/table-of-contents/";
        
      },
    },{id: "post-a-post-with-giscus-comments",
      
        title: "a post with giscus comments",
      
      description: "an example of a blog post with giscus comments",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2022/giscus-comments/";
        
      },
    },{id: "post-a-post-with-redirect",
      
        title: "a post with redirect",
      
      description: "you can also redirect to assets like pdf",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/assets/pdf/example_pdf.pdf";
        
      },
    },{id: "post-a-post-with-diagrams",
      
        title: "a post with diagrams",
      
      description: "an example of a blog post with diagrams",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2021/diagrams/";
        
      },
    },{id: "post-a-distill-style-blog-post",
      
        title: "a distill-style blog post",
      
      description: "an example of a distill-style blog post and main elements",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2021/distill/";
        
      },
    },{id: "post-a-post-with-math",
      
        title: "a post with math",
      
      description: "an example of a blog post with some math",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2015/math/";
        
      },
    },{id: "post-a-post-with-code",
      
        title: "a post with code",
      
      description: "an example of a blog post with some code",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2015/code/";
        
      },
    },{id: "post-a-post-with-images",
      
        title: "a post with images",
      
      description: "this is what included images could look like",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2015/images/";
        
      },
    },{id: "books-21-lessons-for-the-21st-century",
          title: '21 Lessons for the 21st Century',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/21_lessons/";
            },},{id: "books-behave",
          title: 'Behave',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/behave/";
            },},{id: "books-the-book-of-why",
          title: 'The Book of Why',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/book_of_why/";
            },},{id: "books-the-brain",
          title: 'The Brain',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/brain/";
            },},{id: "books-determined",
          title: 'Determined',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/determined/";
            },},{id: "books-incognito",
          title: 'Incognito',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/inocgnito/";
            },},{id: "books-livewired",
          title: 'Livewired',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/livewired/";
            },},{id: "books-noise",
          title: 'Noise',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/noise/";
            },},{id: "books-sapeins",
          title: 'Sapeins',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/sapiens/";
            },},{id: "books-the-tell-tale-brain",
          title: 'The Tell-tale Brain',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/telltale/";
            },},{id: "books-thinking-fast-and-slow",
          title: 'Thinking Fast and Slow',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/thinking_f_n_s/";
            },},{id: "news-a-long-announcement-with-details",
          title: 'A long announcement with details',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/announcement_2/";
            },},{id: "news-talks-at-acs-spring-2025-in-san-diego-about-theoretical-and-experimental-studies-on-redox-active-molecules",
          title: 'Talks at ACS Spring 2025 in San Diego about theoretical and experimental studies...',
          description: "",
          section: "News",},{id: "news-poster-presentation-at-acs-fall-2025-in-washington-dc-about-thermochemical-studies-redox-active-organic-molecules-using-machine-learning",
          title: 'Poster presentation at ACS Fall 2025 in Washington DC about thermochemical studies redox-active...',
          description: "",
          section: "News",},{id: "news-visiting-re-conference-on-renewable-energy-in-las-vegas-come-say-hi",
          title: 'Visiting RE+ conference on renewable energy in Las Vegas, come say hi!',
          description: "",
          section: "News",},{id: "projects-iron",
          title: 'iron',
          description: "mechanistic insights into iron based electron coupled proton buffers [completed]",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-equus",
          title: 'equus',
          description: "ultra-fast screening of redox-active small molecules [completed]",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-lemon",
          title: 'lemon',
          description: "developing a novel molecular generative model [ongoing]",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-tet",
          title: 'tet',
          description: "understanding DNA methylation epigenetics using an inorganic complex [completed]",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_projects/";
            },},{id: "projects-cartpole",
          title: 'cartpole',
          description: "10701 Course Project using Reinforcement Learning [completed]",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-emlip",
          title: 'eMLIP',
          description: "15851 Course Project [ongoing]",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-wait-for-it",
          title: 'wait for it..',
          description: "another project coming soon 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
            },},{id: "summaries-deep-contextualized-word-representations-elmo",
          title: 'Deep contextualized word representations (ELMo)',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-02-deep-contextualized-word-representations/";
            },},{id: "summaries-foundations-and-trends-in-multimodal-machine-learning-principles-challenges-and-open-questions",
          title: 'Foundations and Trends in Multimodal Machine Learning: Principles,  Challenges, and Open Questions',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-02-foundations-and-trends-in-multimodal-machine-learning-principles--challenges-and-open-questions/";
            },},{id: "summaries-bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding",
          title: 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-03-bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/";
            },},{id: "summaries-chain-of-thought-prompting-elicits-reasoning-in-large-language-models",
          title: 'Chain-of-Thought Prompting Elicits Reasoning in Large Language Models',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-03-chain-of-thought-prompting-elicits-reasoning-in-large-language-models/";
            },},{id: "summaries-training-language-models-to-follow-instructions-with-human-feedback-instructgpt",
          title: 'Training language models to follow instructions with human feedback (InstructGPT)',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-05-training-language-models-to-follow-instructions-with-human-feedback/";
            },},{id: "summaries-evaluating-large-language-models-trained-on-code-codex",
          title: 'Evaluating Large Language Models Trained on Code (Codex)',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-06-evaluating-large-language-models-trained-on-code/";
            },},{id: "summaries-bart-denoising-sequence-to-sequence-pre-training-for-natural-language-generation-translation-and-comprehension",
          title: 'BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension',
          description: "",
          section: "Summaries",handler: () => {
              window.location.href = "/summaries/2023-08-09-bart-denoising-sequence-to-sequence-pre-training-for-natural-language-generation-translation-and-comprehension/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%72%73%61%72%6D%61@%61%6E%64%72%65%77.%63%6D%75.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/ronsarma", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/rajdeep-sarma-717a10172", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
