---
tags: go code programming
title: Andy and Teddy are waving goodbye
---

Most of the time, when I've got some software I want to write, I do it in python or sometimes bash. Occasionally though, I like to slip into something with a few more brackets. I've written a bit of C in the past and love it but recently I've been learning [Go](http://golang.org/) and what's really struck me is how clever it is. I'm not just talking about the technical merits of the language itself; it's clever in several areas:

* You don't need to install anything to run Go binaries.

At first - I'm sure like many others - I felt a little revultion when I heard that Go compiles to statically-linked binaries but after having used and played with Go a bit over the past few weeks, I think it's rather clever and was somewhat ahead of the game. In the current climate where DevOps folks (and developers) are getting excited about [containers and componentised services](https://engledow.me/blog/65/), being able to simply [curl](http://curl.haxx.se/) a binary and have it usable in your container without needing to install a stack of dependencies is actually pretty powerful. It seems there's a general trend towards preferring readiness of use over efficiency of space used both in RAM and disk space. And it makes sense; storage is cheap these days. A 10MiB binary is no concern - even if you need several of them - when you have a 1TiB drive. The extravagance of large binaries is no longer so relevant when you're comparing it with your collection of 2GiB bluray rips. The days of needing to count the bytes are gone.

* Go has the feeling of C [but without all that tedious mucking about in <del>hyperspace</del> memory](http://hitchhikers.wikia.com/wiki/Infinite_Improbability_Drive)

Sometimes you just feel you need to write something fairly low level and you want more direct control than you have whilst you're working from the comfort blanket of python or ruby. Go gives you the ability to have well-defined data structures and to care about how much memory you're eating when you know your application needs to process tebibytes of data. What Go doesn't give you is the freedom to muck about in memory, fall off the end of arrays, leave pointers dangling around all over the place, and generally make tiny, tiny mistakes that [take years for anyone to discover](https://en.wikipedia.org/wiki/Heartbleed).

* The build system is designed around how we (as developers) use code hosting facilities

Go has a fairly impressive [set of features](http://golang.org/pkg) built in but if you need something that's not already included, there's a good chance that someone out there has written what you need. Go provides a [package search tool](http://go-search.org/) that makes it very easy to find what you're looking for. And when you've found it, using it is stupidly simple. You add an import declaration in your code:

{% highlight go %}
import "github.com/codegangsta/cli"
{% endhighlight %}

which makes it very clear where the code has come from and where you'd need to go to check the source code and/or documentation. Next, pulling the code down and compiling it ready for linking into your own binary takes a simple:

{% highlight go %}
go get github.com/codegangsta/cli
{% endhighlight %}

Go implicitly understands git and the various methods of retrieving code so you just need to tell it where to look and it'll figure the rest out.

In summary, I'm starting to wonder if Google have a time machine. Go seems to have nicely predicted several worries and trends since [its announcement](http://techcrunch.com/2009/11/10/google-go-language/): Docker, Heartbleed, and social coding.
