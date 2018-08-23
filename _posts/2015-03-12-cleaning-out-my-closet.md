---
tags: arch linux bash
title: Cleaning out my closet
---

Or: *Finding out what crud you installed that's eating all of your space in Arch Linux*

I started running out of space on one of my [Arch](https://www.archlinux.org/) boxes and wondered (beyond what was in my home directory) what I'd installed that was eating up all the space.

A little bit of bash-fu does the job:

{% highlight bash %}
for pkg in $(pacman -Qq); do
    size=$(pacman -Qi $pkg | grep "Installed Size" | cut -d ":" -f 2)
    echo "$size | $pkg"
done | sed -e 's/ //g' | sort -h
{% endhighlight %}

This outputs a list of packages with those using the most disk space at the bottom:

{% highlight console %}
25.99MiB|llvm-libs
31.68MiB|raspberrypi-firmware-examples
32.69MiB|systemd
32.86MiB|glibc
41.88MiB|perl
54.31MiB|gtk2
62.13MiB|python2
73.27MiB|gcc
77.93MiB|python
84.21MiB|linux-firmware
{% endhighlight %}

The above is from my [pi](http://www.raspberrypi.org/); not much I can uninstall there ;)
