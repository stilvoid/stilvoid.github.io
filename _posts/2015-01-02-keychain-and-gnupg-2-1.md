---
title: Keychain and GnuPG >= 2.1
---

A while ago, I started using [keychain](http://www.funtoo.org/Keychain) to manage my ssh and gpg agents. I did this with the following in my `.bashrc`

{% highlight bash %}
# Start ssh-agent
eval $(keychain --quiet --eval id_rsa)
{% endhighlight %}

Recently, [arch](https://www.archlinux.org/) updated gpg to version 2.1.1 which, [as per the announcement](https://www.gnupg.org/faq/whats-new-in-2.1.html), no longer requires the `GPG_AGENT_INFO` environment variable.

Unfortunately, tools like keychain don't know about that and still expect it to be set, leading to some annoying breakage.

My fix is a quick and dirty one; I appended the following to `.bashrc`

{% highlight bash %}
export GPG_AGENT_INFO=~/.gnupg/S.gpg-agent:$(pidof gpg-agent):1
{% endhighlight %}

:)
