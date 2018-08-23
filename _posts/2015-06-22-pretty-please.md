---
title: Pretty please
---

I've been making [a thing](https://github.com/stilvoid/please/) to solve some problems I always face while building web APIs. [Curl](http://curl.haxx.se/) is lovely but it's a bit *too* flexible.

Also, web services generally spit out one of a fairly common set of formats: (json, xml, html) and I often just want to grab a value from the response and use it in a script - maybe to make the next call in a workflow.

So I made [please](https://github.com/stilvoid/please/) which makes it super simple to do things like making a web request and grabbing a particular value from the response.

For example, here's how you'd get the page title from this site:

{% highlight shell %}
please get https://engledow.me/ | please parse html.head.title.#text
{% endhighlight %}

Or getting a value out of the json returned by [jsontest.com](http://jsontest.com/)'s IP address API:

{% highlight shell %}
please get http://ip.jsontest.com/ | please parse ip
{% endhighlight %}

The `parse` part of `please` is the most fun; it can convert between a few different formats. Something I do quite often is grabbing a json response from an API and spitting it out as yaml so I can read it easily. For example:

{% highlight shell %}
please get http://date.jsontest.com/ | please parse -o yaml
{% endhighlight %}

(alright so that's a poor example but the difference is huge when it's a complicated bit of json)

Also handy for turning an unreadable mess of xml into yaml (I love yaml for its readability):

{% highlight shell %}
echo '<docroot type="messydoc"><a><b dir="up">A tree</b><b dir="down">The ground</b></a></docroot>' | please parse -o yaml
{% endhighlight %}

As an example, of the kinds of things you can play with, I made [this tool for generating graphs from json](http://json-graph.offend.me.uk/).

I'm still working on `please`; there will be bugs; [let me know about them](https://github.com/stilvoid/please/issues).
