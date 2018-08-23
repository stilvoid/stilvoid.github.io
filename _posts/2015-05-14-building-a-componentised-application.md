---
tags: docker microservices python
title: Building a componentised application
---

Most of what's here is hardly new ground but I felt it worth noting down the current strategy we're using to develop and build what we're working on at [Proxama](http://www.locationsciences.ai/).

Without going into any of the details, it's a web application with a front end written using [Ember](http://emberjs.com/) and various services that it calls out to, written using whatever seems appropriate per service.

At the outset of the project, we decided we would bite the bullet and build for [Docker](https://www.docker.com/) from the outset. This meant we would get to avoid the usual dependency and developer environment setup nightmares.

## The problem

What we quickly realised as we started to put the bare bones of a few of the services in place, was that we had three seemingly conflicting goals for each component and for the application as a whole.

1. Build images that can be deployed in production.

2. Allow developers to run services locally.

3. Provide a means for running unit tests (both by developers and our CI server).

So here's what we've ended up with:

## The solution

*Or: [docker-compose](http://docs.docker.com/compose/) to the rescue*

### Folder structure

Here's what the project layout looks like:

{% highlight console %}
Project
|
+-docker-compose.yml
|
+-Service 1
| |
| +-Dockerfile
| |
| +-docker.compose.yml
| |
| +-<other files>
|
+-Service 2
  |
  |
  +-Dockerfile
  |
  +-docker.compose.yml
  |
  +-<other files>
{% endhighlight %}

### Building for production

This is the easy bit and is where we started first. The `Dockerfile` for each service was designed to run everything with the defaults. Usually, this is something simple like:

{% highlight dockerfile %}
FROM python:3-onbuild
CMD ["python", "main.py"]
{% endhighlight %}

Our CI server can easily take these, produce images, and push them to the registry.

### Allowing developers to run services locally

This is slightly harder. In general, each service wants to do something slightly different when being run for development; e.g. automatically restarting when code changes. Additionally, we don't want to have to rebuild an image every time we make a code change. This is where `docker-compose` comes in handy.

The `docker-compose.yml` at the root of the project folder looks like this:

{% highlight yaml %}
service1:
    build: Service 1
    environment:
        ENV: dev
    volumes:
        - Service 1:/usr/src/app
    links:
        - service2
        - db
    ports:
        - 8001:8000

service2:
    build: Service2
    environment:
        ENV: dev
    volumes:
        - Service 2:/usr/src/app
    links:
        - service1
        - db
    ports:
        - 8002:8000

db:
    image: mongo
{% endhighlight %}

This gives us several features right away:

* We can locally run all of the services together with `docker-compose up`

* The `ENV` environment variable is set to `dev` in each service so that the service can configure itself when it starts to run things in "dev" mode where needed.

* The source folder for each service is mounted inside the container. This means you don't need to rebuild the image to try out new code.

* Each service is bound to a different port so you can connect to each part directly where needed.

* Each service defines links to the other services it needs.

### Running the tests

This was the trickiest part to get right. Some services have dependencies on other things even just to get unit tests running. For example, [Eve](http://python-eve.org/) is a huge pain to get running with a fake database so it's much easier to just link it to a temporary "real" database.

Additionally, we didn't want to mess with the idea that the images should run production services by default but also didn't want to require folks to need to churn out complicated `docker` invocations like `docker run --rm -v $(pwd):/usr/src/app --link db:db service1 python -m unittest` just to run the test suite after coding up some new features.

So, it was docker-compose to the rescue again :)

Each service has a `docker-compose.yml` that looks something like:

{% highlight yaml %}
tests:
    build: .
    command: python -m unittest
    volumes:
        - .:/usr/src/app
    links:
        - db

db:
    image: mongo
{% endhighlight %}

Which sets up any dependencies needed just for the tests, mounts the local source in the container, and runs the desired command for running the tests.

So, a developer (or the CI box) can run the unit tests with:

{% highlight shell %}
docker-compose run tests
{% endhighlight %}

## Summary

* Each `Dockerfile` builds an image that can go straight into production without further configuration required.

* Each image runs in "developer mode" if the `ENV` environment variable is set.

* Running `docker-compose up` from the root of the project gets you a full stack running locally in developer mode.

* Running `docker-compose run tests` in each service's own folder will run the unit tests for that service - starting any dependencies as needed.
