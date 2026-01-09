---
layout: page
permalink: /courses/
title: courses
description: >
  these are my thoughts on the courses that i took at carnegie mellon university.
nav: false
nav_order: 4
toc:
  sidebar: left
giscus_comments: true
---


Background: i graduated with a [B.S-M.S in chemistry](https://www.iiserb.ac.in/) (2016-2021) from IISER Bhopal concentrating on chemical biology at the [DM Lab](https://www.dmlab.in/). i have preferred taking coures during my undergaduate that pushed me – mathematical methods, statistical mechanics and data science. i have continued that practice at CMU - here is the list of courses

Courses with a &#10084;&#65039; are those that i found transformative.


---

### Spring 2023

{: .first-course-item #course10716 }

- &#11088; 10-716 &nbsp; **[Advanced Machine Learning: Theory and Methods](https://www.cs.cmu.edu/~pradeepr/716/)**, [ Pradeep Ravikumar](http://www.cs.cmu.edu/~pradeepr/)

  This was my favorite class this semester. It felt like a natural
  continuation of [10-708 Probabilistic Graphical Models](#course10708),
  with a strong focus on understanding the theory of how many non-parametric
  modern machine learning techniques work. It is very much a math and theory
  course and can get pretty dense at times, but it is also very rewarding.

  Since there does not appear to be much information online about the specific
  content covered, I'll try to summarize them here.

  1. Statistical decision theory: this was mostly a quick recap,
     since it was covered in the pre-requisite class 36-705.
     If you did not take 36-705, it'll be helpful to learn/review
     Bayesian estimators, and Bayesian and minimax risk as it'll
     be used throughout the course.
  2. Nonparametric Bayesian methods: the Dirichlet process for CDF estimation,
     Dirichlet process mixture for density estimation,
     and the Gaussian process for estimating a regression function
  3. Nonparametric Density Estimation: histograms, kernel density estimators,
     series estimators. A key result is how the kernel estimator is minimax-optimal
     over many classes of loss functions and function spaces.
  4. Nonparametric Regression: partition estimators, spline estimators,
     basis/dictionary series estimators, k-NN regression,
     smoothing kernel regression estimators, Reproducing Kernel Hilbert Space (RKHS)/Mercer kernel regression estimators, wavelets
  5. Nonparametric Classification: contrasting
     classification error between parametric vs nonparametric models,
     minimax rates of convergence for classification vs regression
     for different function classes of distributions
  6. Nonparametric Greedy & Boosting: Orthogonal Greedy Algorithm,
     Greedy Coordinate Descent (i.e boosting), Adaboost,
     functional gradient descent
  7. Optimal Transport: Monge assignments and the Kantorovich relaxation to
     motivate Wasserstein distance, the Kantorovich dual, integral probability
     metrics, applications to statistical estimation and Wasserstein GAN
  8. Deep Density Estimation: variational auto-encoders, normalizing flows, autoregressive flows, destructive distribution learning
  9. Deep Representation Learning and Kernels: RKHS kernel regression, RKHS in
     relation to representation learning, random features, randomly wired DNNs and
     its relation to Gaussian Processes
  10. Dimensionality Reduction & Manifolds: PCA, multi-dimensional scaling
      (MDS), kernel PCA, local linear embeddings (LLE), Laplacian eigenmaps,
      diffusion maps, Johnson-Lindenstrauss Lemma and random projections
  11. Clustering: k-means as vector quantization, mixture models and local non-identifiability,
      level set clustering, hierarchical clustering, spectral clustering
  12. Learning & Games: online learning, Follow the Leader (FTL), Follow the Regularized Leader (FTRL),
      regret bounds for FTRL on convex and non-convex action domains and loss functions, two-player games and Nash equilibrium
  13. Causality: adjusting for confounding, causal graphs and structural equations
  14. Random Forests and Kernels: Bagging, layered nearest neighbor (LNN), kernel-based view of random forests

  Pradeep is a great lecturer and he takes great effort to answer every student's questions in detail.
  However, while I often find myself being able to follow the current micro-level derivations and explanations,
  I often feel somewhat lost about how it fits in with the bigger picture and its relation with other techniques,
  possibly due to a lack of prior exposure to many of these topics.

  There is significant variance in the difficulty of homework problems in a
  single homework, which I thought made the scoring of the homework problems
  somewhat nonsensical as the points were more or less evenly distributed. I
  recall there were a couple of problems that demanded a fair bit of thought and
  insight but had relatively short solutions, and therefore only netted a
  moderate amount of points compared to the effort required.

  I thought the exams were relatively easy. It is proof-based and will ask you
  to perform derivations of results or techniques related to what is seen in class,
  which sounds much scarier than it actually is because the questions are relatively guided.

  One thing that happened this semester (and also apparently for prior semesters
  according to some people that I spoke to) was the steep drop in attendance as the semester
  went on. During the first lecture, there were barely enough seats for everyone
  and some people had to stand, but by the mid-way point the average attendance was
  just around 5 people. However, when it came to the midterms, the classroom filled up again
  and I even heard the instructor for the previous class remark how she didn't
  realize we had so many students in this class as she was leaving.

  This was probably not such a bad thing for the people who did come to lectures, since
  it meant more personalized attention from the instructor, more opportunities
  to ask your own questions, and a better view of the board.

  I initially thought this phenomenon was because the other students (who were
  mostly MLD Ph.Ds and MSML/MSDS students) were already very knowledgeable and didn't see the need to
  come to lecture, but only learned much later that it was actually because many
  of them also found the material challenging and found it difficult to follow the lecture.

  I think the takeaway here is that this will be a very difficult class (in my opinion likely
  the hardest class offered in MLD), so try to go in with friends and don't shy away
  from asking questions since it is likely that many people may also be confused.

- &#10084;&#65039; 36-709 &nbsp; **Advanced Statistical Theory I**, [Matey Neykov](https://mateyneykov.com/)
  {: .course-item #course36709 }

  This course largely follows [High-Dimensional Statistics: A Non-Asymptotic Viewpoint](https://www.cambridge.org/core/books/highdimensional-statistics/8A91ECEEC38F46DAB53E9FF8757C7A4E) by [Wainwright](https://people.eecs.berkeley.edu/~wainwrig/),
  with the last portion branching off towards topics in the professor's own research interests.
  This is a core course in theoretical statistics that all stats Ph.D students
  must take, and most students in the course came from this demographic. The
  focus of the course is on high-dimensional statistical models, and
  non-parametric statistical models.

  There were 4 homeworks, with around 2-3 weeks between each one. They are all proof-based questions, with many
  of them coming from Wainwright's book. I found the homeworks quite challenging, and had to collaborate with
  a few stats Ph.D students to get through some of them (thank you for
  introducing me to the stats Ph.D. lounge!). There were some tools required
  for solving some of the problems that I have never seen or had to use before
  in any of my previous CS or math classes, but which may (?) be standard fare in
  statistical literature, that may have contributed to my difficulty.
  Fortunately, I still managed to solve _almost_ all the homework problems.

  Each student also had to scribe a lecture, which is then posted on Canvas as
  reference for all other students. There is also a project on deeply understanding a
  recent advanced theoretical paper in statistics or machine learning, which involves
  both a paper writeup and a presentation of its contents to the class.
  Thankfully there are no exams.

  Topics covered included concentration inequalities (sub-Gaussian,
  sub-exponential random variables), maximal inequalities, bounded differences,
  covering and packing, Gaussian and Rademacher complexity, chaining and
  Dudley's entropy integral bound, comparison inequalities (Slepian and
  Sudakov-Fernique) and lower bounds, high-dimensional and sparse PCA,
  Davis-Kahan theorem, LASSO in relation to prediction/support recovery/debiasing,
  covariance matrix estimation, non-parametric least squares, minimax lower
  bounds (Le Cam's method and Fano's method), Gaussian sequence model minimax rates.

  Overall I really enjoyed this class as it introduced me to many concepts in
  modern statistical analysis, which is really helpful in understanding
  statistical machine learning papers.

- 36-708 &nbsp; **[The ABCDE of Statistical Methods in Machine Learning](https://36708.github.io/)**, [Aaditya Ramdas](https://www.stat.cmu.edu/~aramdas/)
  {: .course-item #course36708 }

  I initially did not notice this course, as I thought ABCDE meant just the basics.
  However, what the course is actually about is a journey through various
  methods in statistical machine learning, viewed from the following lens:

  - **A**lgorithm design principles,
  - **B**ias-variance trade-off,
  - **C**omputational and memory considerations, **C**alibration, **C**onformal prediction,
  - **D**ata analysis,
  - **E**xplainability and interpretability.

  Aaditya is really clear, and he will re-iterate the important
  points many times throughout the class, sometimes too many times in my opinion,
  which was fine but it would also be good to learn more content instead. I
  also heard from some other students that he is one of the best lecturers in
  the stats department.

  Most of the class is on non-parametric methods, covering
  techniques like nearest neighbor methods, distribution-free predictive inference,
  calibration, decision trees, bagging, random forests, stacking, boosting,
  reproducing kernel Hilbert spaces (RKHS), kernel methods like kernel
  ridge regression and kernel PCA, Shapley values, spectral PCA,
  and some basic deep learning topics like deep PCA.

  I found the class very practical and helpful, and learned a lot as someone
  with no data science and practical machine learning background. This was
  especially from the many discussions on which techniques were suitable for
  which contexts, according to the ABCDE methodology.

  A lot of the topics in this course were familiar to other students who came
  from a traditional stats background, and I feel like you might get bored in
  this class if you already have a pretty solid stats foundation. Otherwise,
  there is a lot you'll learn.

  The midterms and homework were both relatively chill. Homework included both
  theoretical derivations, and also experiments on datasets using methods
  learned in class.

- 21-329 &nbsp; **Set Theory**, Benjamin Siskind
  {: .course-item #course36708 }

  I initially got interested in this class as quite a couple of theorems from my
  other classes appealed to important results from set theory, such as Zorn's
  Lemma used for proving Tychonoff's theorem. Since set theory is such a foundational
  topic in mathematics, I wanted to take it to satisfy my curiosity.

  This course covered all the chapters in [A Course on Set Theory](https://www.cambridge.org/core/books/course-on-set-theory/9E65D5D9CA561CA2D87F91B21B0D117D)
  apart from 6, i.e ZFC, order, cardinality, trees, and filters and ideals.
  It starts fairly slowly, and speeds up towards the latter of the second
  half. I could see some parallels between set theory and type theory
  initially in the more constructive concepts, but they soon began to differ
  greatly due to the heavy use of non-constructive methods
  in the proofs of set theory.

  The most interesting topic for me was the development of trees and Baire
  spaces, which led to the study of games and determinacy,
  with the consequence that sets which are determined have certain nice
  properties.

  The course was taught by Benny, a postdoctoral associate teaching the class
  for the first time, so it was expected that there would be a few rough edges.
  Benny cares about the class, is passionate about the course content (he
  does research in model theory and descriptive set theory), and responds to
  emails and clarifications fairly promptly.

  I think the course could have been paced faster at the start. It was also
  challenging to read the lecturer's handwriting sometimes. I felt there was
  significant time pressure for the exams (similar to [21-301
  Combinatorics](#course21301)), though the homeworks were quite reasonable.

- 17-604 &nbsp; **Communications for Software Leaders II**, [Dominick (Nick) Frollini](https://www.linkedin.com/in/frollini/)
  {: .course-item #course17604 }

  The highlight of this follow-up class to
  [17-603 Communication for Software Leaders I](#course17603) are the mock
  negotiation in-class exercises that we had to prepare and role-play for.
  Prior to each mock negotiation, we were provided with case
  materials developed by the
  [Kellogg](https://www.kellogg.northwestern.edu/) MBA program that contains
  important private information specific to our role, which must
  be kept secret.
  We then planned out our negotiation strategy before class, possibly with
  other people in the same faction so as to present a unified front
  against the other parties during negotiation.

  The mock negotiations were really exciting as they put us in the shoes
  of roles as diverse as CEOs, government officials, hardware designers,
  or even fishermen. You will have specific instructions on
  the kind of personality traits, negotiation style, and cultural
  customs that your role will have. I really indulged myself in this,
  especially since I took [70-350 Acting for Business](#course70350)
  not too long ago. The outcome of the negotiations will directly
  affect your grades, so these are really high-stakes, high-pressure
  situations that you will be put into. It was extremely fun and
  entertaining.

  Nick is a very passionate teacher with clear and well-paced lectures.
  It's obvious he has done this so many times that it's almost
  like a rehearsed performance. In my opinion, if you are already
  planning to take [17-603](#course17603), then you must take
  this course as well since the mock negotiations were so much fun.

Units: 60

This was the final semester (out of 2) of my Master's degree. My
goal for pursuing a M.S degree is to reach the frontiers of a field
and find a research interest, which I did in theoretical machine learning.
I mostly leave without regrets, except for one: not having been able to
work with any of the brilliant professors here on research, since I found
my direction so late.

I TA'd for [10-708 Probabilistic Graphical
Models](https://andrejristeski.github.io/10708-S23/) under [Andrej
Risteski](https://www.andrew.cmu.edu/user/aristesk/) this semester.
It was a fun experience and not as stressful as I had feared. Being
able to lead 2 of the recitations was one of the highlights of my semester.
I would like to thank [Andrej](https://www.andrew.cmu.edu/user/aristesk/) and my
fellow TAs (especially [Jennifer](https://scholar.google.com/citations?user=4i-T-5UAAAAJ), whose
office hours slot was right before mine and always stayed overtime
to help me with the queue) for making it so enjoyable. I am also
grateful to all my students for their great questions and being able to mentor
their impressive projects, and for giving me the opportunity to grow as a TA.

I also continued staying in an advisory role for
[Autolab](https://autolabproject.com/), being generally quite hands-off.
[Michelle](https://michellexliu.me/) was the project lead this semester and did
a terrific job. This being my last semester, I will dearly miss the team when I
graduate.

I did booth with [SSA](https://cmussa.org/) again this year, and contributed mainly
to the mechanical team and design teams. We built a Blitz booth themed after Singapore's
[Gardens by the Bay](https://www.gardensbythebay.com.sg/) and came in runner's up, after
a well-deserved win by [JSA](https://www.cmujsa.com/).

Academically, this semester was rather risky for me because I did not have the necessary
prerequisites for over half of my classes. I was missing
[36-705 Intermediate Statistics](https://www.stat.cmu.edu/~larry/=stat705/)
for [10-716](#course10716), [36-708](#course36708), [36-709](#course36709),
and missing [21-720 Measure Theory and Integration](https://www.math.cmu.edu/~gautam/sj/teaching/2022-23/720-measure/) for [21-640].
It was also a difficult and tiring process to get into [36-709](#course36709) as
the class was a required stats Ph.D. course that was generally very full, and
they had no reservations for CS majors. I ended up reading through some of the
lecture notes of [36-705](https://www.stat.cmu.edu/~larry/=stat705/)
over the winter break before the semester began to insure against the worst-case
scenario.

I ended up dropping 21-640 Functional Analysis halfway through the semester
as it became increasingly difficult to do (and even understand) the homework without
the necessary measure theory background.
While 21-720 was not listed as a prerequisite
on SIO for this course, it was announced as such (along with [21-640 General
Topology](#course21640)) by the instructor during the first class, so as to
motivate and develop many of the more interesting applications in the subject.

This concludes my wonderful time at CMU, and I leave with many beautiful
memories. Thank you to my professors who showed me the bountiful fields of their
intellectual gardens and sparked a lifelong joy and insatiable desire in this
student of wanting to explore more of it; to my friends who colored my life with
love and laughter through our journey of growth and humility, I hope we will
stay lifelong friends; and finally to my family for always being so
unconditionally supportive and for providing a safe harbor for me to turn to any
time.

### Fall 2022

{: .first-course-item #course15859CC }

- &#11088; 15-859 CC &nbsp; **[Algorithms for Big Data](https://www.cs.cmu.edu/~dwoodruf/teaching/15859-fall22/index.html)**, [David Woodruff](http://www.cs.cmu.edu/~dwoodruf/)

  Woodruff is one of the giants in sketching and numerical linear algebra, having developed many of its most important algorithms.
  There is even a `sklearn` function called the [Clarkson-Woodruff transform](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.clarkson_woodruff_transform.html) that is named after him.

  His teaching is extremely clear as he makes sure to justify and explain every step used in a proof. The analysis for many
  sketching algorithms is highly non-trivial, but Woodruff manages to pull off explaining it in a way that reads like a storybook.
  He cares deeply about the class and the student's learning, and one thing that still amazes me to this day is how he will respond to my
  Piazza questions on a weekend in 2 minutes consistently. I even made a [meme about it](https://t.co/zSg7KwmJkN).

  The homework problems are long but rewarding, and you will become intimately
  familiar with all sorts of linear algebra manipulations and properties.

  One caveat is that the weekly lectures are 3-hours with a 10-minute break in the middle. Given how dense the lectures are, this can be quite
  taxing, so bring snacks or caffeine if needed.

