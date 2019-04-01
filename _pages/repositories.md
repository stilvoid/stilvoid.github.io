---
title: Repositories
permalink: /projects/
---
{% for repository in site.github.public_repositories %}
{% endfor %}

In order of most recently updated:

<ul class="post-list">
{% assign sorted_repos = site.github.public_repositories | sort:"updated_at" | reverse %}
{% for repository in sorted_repos %}
    <li>
        <span class="post-meta">{{repository.updated_at | date:"%Y-%m-%d"}}</span>
        <h3>
            <a class="post-link" href="{{ repository.html_url }}">{{repository.name}}</a>
        </h3>
        <p>
            {{ repository.description }}
        </p>
    </li>
{% endfor %}
<ul>
