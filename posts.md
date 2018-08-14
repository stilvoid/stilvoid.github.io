---
title: Stilvoid's Posts
---

{% for post in site.posts %}
* <span class="post-meta">{{post.date | date:"%Y-%m-%d"}}</span> [{{ post.title }}]({{ post.url }})

    {{post.excerpt}}

{% endfor %}
