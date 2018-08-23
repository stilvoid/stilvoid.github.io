---
tags: linux desktop editors
title: An evening of linux on the desktop
---

[Last time](https://engledow.me/blog/88/), I wrote about trying a few desktop environments to see what's out there, keep things fresh, and keep me from complacency. Well, as with desktop environments, so with text editors. I decided briefly that I would try [a few of](https://atom.io/) [the more recent](https://www.sublimetext.com/) [code editors](https://code.visualstudio.com/) that are around these days. Lured in by their pleasing, modern visuals and their promises of a smooth, integrated experience, I've been meaning to give these a go for a while. Needless to say, as a long-time [vim](https://www.vim.org/) user, I just found myself frustrated that I wasn't able to get things done as efficiently in any of those editors as I could in vim ;) I tried installing vim keybindings in Atom but it just wasn't the same as a very limited set of functionality was there. As for the integrated environment, when you have [tmux running by default](https://engledow.me/blog/46), everything's integrated anyway.

And, as with editors, so once again with desktop environments. I've decided to retract my previous hasty promise and no longer to bother with trying any other environments; [i3](https://i3wm.org/) is more than fine :)

However, I did spend some time this evening making things a bit prettier so here are some delicious configs for posterity:

## Configs

### Xresources

I've switched back to xterm from urxvt because, er... dunno.

Anyway, I set some nice colours for terminals and some magic stuff that makes man pages all colourful :)

{% highlight config %}
XTerm*faceName: xft:Hack:regular:size=12
*termName: xterm-256color

! Colourful man pages
*VT100.colorBDMode:     true
*VT100.colorBD:         cyan
*VT100.colorULMode:     true
*VT100.colorUL:         darkcyan
*VT100.colorITMode:     true
*VT100.colorIT:         yellow
*VT100.veryBoldColors:  518

! terminal colours
*foreground:#CCCCCC
*background:#2B2D2E

!black darkgray
*color0:    #2B2D2E
*color8:    #808080
!darkred red
*color1:    #FF0044
*color9:    #F92672
!darkgreen green
*color2:    #82B414
*color10:   #A6E22E
!darkyellow yellow
*color3:    #FD971F
*color11:   #E6DB74
!darkblue blue
*color4:    #266C98
*color12:   #7070F0
!darkmagenta magenta
*color5:    #AC0CB1
*color13:   #D63AE1
!darkcyan cyan
*color6:    #AE81FF
*color14:   #66D9EF
!gray white
*color7:    #CCCCCC
*color15:   #F8F8F2
{% endhighlight %}

### Vimrc

Nothing exciting here except for discovering a few options I hadn't previous known about:

{% highlight vim %}
" Show a marker at the 80th column to encourage nice code
set colorcolumn=80
highlight ColorColumn ctermbg=darkblue

" Scroll the text when we're 3 lines from the top or bottom
set so=3

" Use browser-style incremental search
set incsearch

" Override the default background colour in xoria256 to match the terminal background
highlight Normal ctermbg=black

" I like this theme
colorscheme xoria256
{% endhighlight %}

### i3

I made a few colour tweaks to my i3 config so I get colours that match my new Xresources. One day, I might see if it's easy enough to have them both read colour definitions from the same place so I don't have to define things twice.

## The result

Here's what it looks like:

[![My new desktop](https://static.offend.me.uk/media/images/blog/89/01-small.jpg)](https://static.offend.me.uk/media/images/blog/89/01.jpg)
