---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% assign citations_endpoint = site.url | append: site.baseurl | append: '/assets/json/citations.json' | url_encode %}

I have published 5 first-author research papers with total <a href="https://scholar.google.com/citations?user=8-IhrB0AAAAJ">
  <img src="https://img.shields.io/badge/citations-102-9cf?logo=Google%20Scholar&labelColor=f6f6f6&style=flat" alt="Google Scholar citations">
</a>

{% include base_path %}

{% for post in site.publications reversed %}
    {% include archive-single.html %}
{% endfor %}
