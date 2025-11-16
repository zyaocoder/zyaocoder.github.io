---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


I have published 5 first-author research papers with total <a href='https://scholar.google.com/citations?user=8-IhrB0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

You can also find my articles on my [Google Scholar profile](https://scholar.google.com/citations?user=8-IhrB0AAAAJ&hl=en&oi=ao>).

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
    {% include archive-single.html %}
{% endfor %}
