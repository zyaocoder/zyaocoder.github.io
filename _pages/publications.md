---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---



You can also find my articles on my [Google Scholar profile](https://scholar.google.com/citations?user=8-IhrB0AAAAJ&hl=en&oi=ao>).

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      {% if post.venue %}
      <div class="badge">{{ post.venue }}</div>
      {% endif %}

      {% if post.image %}
      <img src='{{ post.image | relative_url }}'
           alt="{{ post.title | escape }}"
           width="100%">
      {% endif %}
    </div>
  </div>

  <div class='paper-box-text' markdown="1">
    {% include archive-single.html %}
  </div>
</div>
{% endfor %}
