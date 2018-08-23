---
tags: code web aws
title: Digital Subscriber
---

Maybe it's just me, but I reckon [DSLs](https://en.wikipedia.org/wiki/Domain-specific_language) are the next (ok ok, they've been around for ages) big (ok, hipster) thing. I know I'm by no means the first to say so it's just that I'm increasingly bemused at seeing things squeezed into data structures they've outgrown.

In general, as everyone's finally warming to the idea that you can use code to describe not just your application but also how it's deployed, we're reaching a state where that code needs to be newbie-friendly - by which I mean that it ought to be easily understandable by humans. If it isn't, it's prone to mistakes.

A few months ago, I experimented with creating a DSL for writing web pages and I was fairly happy with [the result](https://github.com/stilvoid/thiy) (though there's lots more work to be done). I'm thinking of applying the same ideas to [CloudFormation](https://aws.amazon.com/cloudformation/).

{% highlight yaml %}
resources:
    db:
        type: rds
        engine: mysql
        size: c3.xlarge

    app:
        type: ec2
        ami: my-app-image
        size: t2.micro
        scale:
            min: 1
            max: 10
        expose: 80

security:
    db: app
    app: 0.0.0.0:80
{% endhighlight %}

Obviously I've put little to no thought into the above but it shouldn't be too hard to come up with something useful.

Maybe some day soon ;)
