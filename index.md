I'm Steve Engledow, senior solutions builder at [AWS Professional Services](https://aws.amazon.com/professional-services/).

![Picture of Steve Engledow](https://static.offend.me.uk/media/images/me-real-small.jpg)

All views expressed here are my own and don't necessarily reflect Amazon's :)

## Fact sheet

Just the important details:

* I use [Arch Linux](https://www.archlinux.org/) and prefer [vim](https://www.vim.org/) over [emacs](http://www.wikivs.com/wiki/Vim_vs_Emacs).

* [Here's my Amazon wishlist](http://www.amazon.co.uk/registry/wishlist/12CD3CY66XFWK).

* [Here](https://www.politicalcompass.org/printablegraph?ec=-4.75&soc=-4.56)'s where I am on [the political compass](https://www.politicalcompass.org/).

* Various [personality test](https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator)s have me down as [INTP](https://en.wikipedia.org/wiki/INTP).

* Alignment: [Neutral good](https://en.wikipedia.org/wiki/Alignment_(Dungeons_%26_Dragons)#Neutral_good).

Anything else is hearsay.

## Recently-updated Projects

{% assign sorted_repos = site.github.public_repositories | sort:"updated_at" | reverse %}
{% for repository in sorted_repos limit:10 %}
* <span class="post-meta">{{repository.updated_at | date:"%Y-%m-%d"}}</span> [{{ repository.name }}]({{ repository.html_url }})
{% endfor %}

[All projects](/projects/)

## Recent Posts

{% for post in site.posts limit:10 %}
* <span class="post-meta">{{post.date | date:"%Y-%m-%d"}}</span> [{{ post.title }}]({{ post.url }})
{% endfor %}

[All posts](/posts/)
