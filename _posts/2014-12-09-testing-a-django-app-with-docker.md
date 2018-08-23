---
tags: proxama docker django
title: Testing a Django app with Docker
---

I've been playing around with Docker a fair bit and recently hit upon a configuration that works nicely for me when testing code at work.

The basic premise is that I run a docker container that pretty well emulates the exact environment that the code will run in down to the OS so I don't need to care that I'm not running the same distribution as the servers we deploy to and that I can test my code at any time without having to rebuild the docker image.

Here's an annotated [Dockerfile](http://docs.docker.com/reference/builder/) with the project-specific details removed.

{% highlight dockerfile %}
# We start with ubuntu 14.04

FROM ubuntu:14.04
MAINTAINER Steve Engledow <steve@engledow.me>

USER root

# Install OS packages
# This list of packages is what gets installed by default
# on Amazon's Ubuntu 14.04 AMI plus python-virtualenv

 RUN apt-get update \
     && apt-get -y install software-properties-common git \
     ssh python-dev python-virtualenv libmysqlclient-dev \
     libqrencode-dev swig libssl-dev curl screen

# Configure custom apt repositories
# and install project-specific packages

COPY apt-key.list apt-repo.list apt.list /tmp/

# Not as nice as this could be as docker defaults to sh rather than bash
RUN while read key; do curl --silent "$key" | apt-key add -; done < /tmp/apt-key.list
RUN while read repo; do add-apt-repository -y "$repo"; done < /tmp/apt-repo.list
RUN apt-get -qq update
RUN while read package; do apt-get -qq -y install "$package"; done < /tmp/apt.list

# Now we create a normal user and switch to it

RUN useradd -s /bin/bash -m ubuntu \
    && chown -R ubuntu:ubuntu /home/ubuntu \
    && passwd -d ubuntu

USER ubuntu
WORKDIR /home/ubuntu
ENV HOME /home/ubuntu

# Set up a virtualenv andinstall python packages
# from the requirements file

COPY requirements.txt /tmp/

RUN mkdir .myenv \
    && virtualenv -p /usr/bin/python2.7 ~/.myenv \
    && . ~/.myenv/bin/activate \
    && pip install -r /tmp/requirements.txt \

# Set PYTHONPATH and activate the virtualenv in .bashrc

RUN echo "export PYTHONPATH=~/myapp/src" > .bashrc \
    && echo ". ~/.myenv/bin/activate" >> .bashrc

# Copy the entrypoint script

COPY entrypoint.sh /home/ubuntu/

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
{% endhighlight %}

And here's the entrypoint script that nicely wraps up running the django application:

{% highlight bash %}
#!/bin/bash
. ./.bashrc
cd myapp/src
./manage.py $*
{% endhighlight %}

You generate the base docker image from these files with `docker build -t myapp ./`.

Then, when you're ready to run a test suite, you need the following invocation:

{% highlight shell %}
docker run -ti --rm -P -v ~/code/myapp:/home/ubuntu/myapp myapp test
{% endhighlight %}

This mounts `~/code/myapp` and `/home/ubuntu/myapp` within the Docker container meaning that you're running the exact code that you're working on from inside the container :)

I have an alias that expands that for me so I only need to type `docked myapp test`.

Obviously, you can substitute `test` for `runserver`, `syncdb` or whatever :)

This is all a bit rough and ready but it's working very well for me now and is repeatable enough that I can use more-or-less the same script for a number of different django projects.
