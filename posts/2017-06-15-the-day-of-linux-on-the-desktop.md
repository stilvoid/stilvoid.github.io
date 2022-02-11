---
tags: linux desktop
title: The day of linux on the desktop
---

It's been a while since I last tried out a different desktop environment on my laptop and I've been using [i3](https://i3wm.org/) for [some time now](https://engledow.me/blog/01/) so it's only fair to give other things a go ;)

To test these out, I ran another X display - keeping my original one running so I could switch back and forth to take notes - and started each environment with `DISPLAY=:1 <the command to start the desktop>`.

I'll start with just one today and perhaps review some others another time.

## Deepin

In summary: bits of Gnome Shell, Chrome OS, and Mac OSX but not quite as polished as any of them.

The Deepin Desktop Environment (DDE - from [the Deepin distribution](https://www.deepin.org/en/?language=en)) installed easily enough under Arch with a quick `pacman -S deepin deepin-extra`. It also started up easily with an unambiguous `startdde`.

Immediately on startup, DDE plays a slightly annoying chime presumably just to remind you of how far we've come since Windows 95. The initial view of the desktop looks similar to OSX or Chrome OS with file icons on the desktop and a launcher bar centred across the bottom of the screen.

![The initial view](https://static.offend.me.uk/media/images/blog/88/01.jpg)

The first thing I tried was clicking on a button labelled "Multitasking view" only to be presented with a prompt telling me "Kindly reminder: This application can not run without window effect" and an OK button. So far, so enigmatic. So then I tried a trusty right-click on the desktop which brought up the expected context menu. In the menu was a "Display settings" option so I plumped for that, thinking that perhaps that was where I could enable the mystic "window effect". Clicking the "Display settings" button opened a dark-themed panel from the right-hand side, similar to the information panel you get in OSX. I searched through that panel for a good couple of minutes but could find no allusion to any "window effect".

![The cryptic message and the settings panel](https://static.offend.me.uk/media/images/blog/88/02.jpg)

Unperturbed, I decided to press on and see what other features Deepin had to offer...

Moving the mouse around the desktop a bit, I discovered that Deepin has borrowed some ideas from Gnome shell as well as OSX and Chrome OS. Moving the mouse pointer into the top-left corner of the screen brings up an application list similar to Gnome's launcher. The bottom-right corner reveals the settings panel. The top-right does nothing and the bottom-left, wonder of wonders, brings up my old favourite, the "kindly reminder".

I poked around in the settings a bit more but didn't really see anything of interest so I fired up what looks to be the last part of Deepin left for me to explore: the file manager. It does the job and it's not very interesting although I did discover that Deepin also has it's own terminal emulator (unsurprisingly called `deepin-terminal`) which has a snazzy [Matrix](https://en.wikipedia.org/wiki/The_Matrix) theme to it but is otherwise uninteresting.

![Deepin-terminal](https://static.offend.me.uk/media/images/blog/88/03.jpg)

That's it, I'm bored. Next!

I tried Budgie and LXQT for a few minutes each at this point but they weren't immediately interesting enough to make me want to write about them just now :)