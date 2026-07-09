---
layout: default
---

<div class="hero">
  <div class="hero-text">
    <p class="tagline">I'm a <span class="tagline-em">cognitive scientist</span> studying <span class="tagline-em">human&ndash;AI collaboration</span>: when partnerships with AI work, when they erode human skill, and how AI can strengthen human connection.</p>
    <p class="tagline"><i class="fa-solid fa-bullhorn" aria-hidden="true"></i> I'm on the 2026&ndash;27 job market! </p>  
    <ul class="quick-links">
      <li><a href="CV.pdf" target="_blank"><i class="fa-solid fa-file-lines" aria-hidden="true"></i> CV</a></li>
      <li><a href="https://scholar.google.com/citations?user=XFM1ItgAAAAJ&hl=en"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i> Scholar</a></li>
      <li><a href="mailto:aakriti1kumar@gmail.com"><i class="fa-solid fa-envelope" aria-hidden="true"></i> Email</a></li>
      <li><a href="https://github.com/aakriti1kumar"><i class="fa-brands fa-github" aria-hidden="true"></i> GitHub</a></li>
      <li><a href="https://www.linkedin.com/in/aakriti1kumar/"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i> LinkedIn</a></li>
    </ul>
  </div>
  <img class="hero-photo" src="profile.jpg" alt="Aakriti Kumar" />
</div>

<p>I'm a cognitive scientist studying human&ndash;AI collaboration, focused on the interplay between metacognition and AI. I'm currently a Postdoctoral Researcher at the <a href="https://www.kellogg.northwestern.edu/">Kellogg School of Management</a> and the <a href="https://www.nico.northwestern.edu/">Northwestern Institute on Complex Systems (NICO)</a>, working with <a href="https://mattgroh.com/">Dr. Matt Groh</a>, where I build tools to support human communication and design AI evaluations that support human metacognition. I run large-scale lab, digital, and field experiments in real-world settings, combining behavioral data with computational and qualitative analysis. My research spans organizational behavior, AI, and human&ndash;computer interaction.</p>

<p>I earned my PhD in Cognitive Science from UC Irvine, advised by <a href="https://steyvers.socsci.uci.edu/">Dr. Mark Steyvers</a>, along with an MS in Statistics from UCI and a B.Tech. from IIT Madras. My PhD research explored how people infer what a human or an AI collaborator knows, how good they are at a task, and when to rely on their advice. Using hierarchical Bayesian and item response theory models, I showed that the mental models people build of AI differ systematically from those they build of other humans; for example, people who accurately gauge another person's abilities consistently overestimate an AI's. Along the way, I've also worked in industry at Honda Research Institute and Motional (a robotaxi startup), and collaborated with researchers at Google Research India.</p>

<p>I'm always happy to chat about research, please <a href="mailto:aakriti1kumar@gmail.com">reach out</a>!</p>

<h2 class="section-head">Selected work</h2>

<div class="work-grid">
{% for w in site.data.selected_work %}
  <div class="work-card">
    <h3><a href="{{ w.link }}">{{ w.short_title | default: w.title }}</a></h3>
    <span class="venue-pill {% if w.status == 'review' %}pill-review{% else %}pill-pub{% endif %}">{{ w.venue }}</span>
    {% if w.figure %}<img class="card-fig" src="{{ w.figure }}" alt="{{ w.figure_alt | default: w.title }}" />{% endif %}
    {% if w.demo_link %}<p class="card-demo"><a href="{{ w.demo_link }}">{{ w.demo_text }} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a></p>{% endif %}
  </div>
{% endfor %}
</div>

<p class="see-all">See all publications on <a href="projects">the research page</a> or <a href="https://scholar.google.com/citations?user=XFM1ItgAAAAJ&hl=en">Google Scholar</a>.</p>


<h2 class="section-head">News</h2>

<div class="news-strip">
{% for n in site.data.news %}
  <div class="news-panel">
    <span class="news-date">{{ n.date }}</span>
    <p class="news-text">{{ n.text }}</p>
    {% if n.embed %}<iframe class="news-embed" src="{{ n.embed }}" frameborder="0" allowfullscreen title="Embedded LinkedIn post"></iframe>{% endif %}
    {% if n.link %}<a class="news-link" href="{{ n.link }}">{% if n.linkedin %}<i class="fa-brands fa-linkedin-in" aria-hidden="true"></i> {% endif %}{{ n.link_text | default: "Read more" }} &rarr;</a>{% endif %}
  </div>
{% endfor %}
</div>
<p class="news-hint"><i class="fa-solid fa-arrow-right-arrow-left" aria-hidden="true"></i> Scroll sideways for more news</p>
