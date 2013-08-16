# tyler

## Build Status

![current build status](https://travis-ci.org/codersquid/tyler.png?branch=master) (still figuring out how to set up travis env to work with postgres)

[build history](https://travis-ci.org/codersquid/tyler)

## Intro

This repo contains a skeleton Django project that is deployable on Heroku or on
a local or remote machine. Static files are served locally in DEBUG mode or via
S3 when deployed to Heroku and/or in non-DEBUG mode.

I've set up a [trello](https://trello.com/b/8KC8wAye/rmc) board and have also
created [issues](https://github.com/codersquid/tyler/issues) in the github tracker.
I'm trying out both tools to see which is most useful, I may find a tool to link them up
in case they both are. I wish there was a trello-like UI for the github tracker.

(I'm starting not to like trello for tracking things. I like issue trackers more.)

## Site Design

This is entirely in flux but I want to at least splat some links here

#### custom apps

* `results`: this will stay empty until we get to the point where we want to show history pages with the results of runs
* `status`: this will stay empty until we get to the point where we want a site status page with status news, graphs, etc. actually, I should probably rip this out and make a static page and stick it on another webserver entirely? I'll figure that out.

#### third party docs

* [django-model-utils](https://django-model-utils.readthedocs.org/en/latest/)
* [django-storages, s3](http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html) see also heroku docs on [django static assets](https://devcenter.heroku.com/articles/django-assets)
* [django-profiles](https://bitbucket.org/ubernostrum/django-profiles)
   * waiting on [pull request](https://bitbucket.org/ubernostrum/django-profiles/pull-request/6/replaced-profile_list-view-with-a-class/diff) which is why requirements point directly to fcurella's zip
   * [blog post, slightly outdated but helpful](http://birdhouse.org/blog/2009/06/27/django-profiles/)
* [django-registration](https://bitbucket.org/ubernostrum/django-registration) and a [blog post](http://www.michelepasin.org/blog/2011/01/14/setting-up-django-registration/)
* [django-envelope](http://django-envelope.readthedocs.org/en/latest/index.html)
* [boostrap](http://getbootstrap.com/)
* my bookmarks tagged with [tyler](https://pinboard.in/u:sky/t:tyler/) that includes the above and more


## Working Environment

To set up a working environment,

* `git clone git@github.com:codersquid/tyler.git`
* `cd tyler`
* `virtualenv venv`
* `source venv/bin/acivate`
* `pip install -r requirements.txt`

You need to define environment variables to run this locally.

```
export SECRET_KEY=''
export DEBUG='True'
export ADMINS=''
export SITE_ID=1
export DATABASE_URL=''
export MAILGUN_ACCESS_KEY=''
export MAILGUN_SERVER_NAME=''
export EMAIL_BACKEND=''
export AWS_ACCESS_KEY_ID=''
export AWS_SECRET_ACCESS_KEY=''
export AWS_STORAGE_BUCKET_NAME=''
export DEFAULT_FROM_EMAIL=''
export ENVELOPE_EMAIL_RECIPIENTS=''
export PORT=8000
```

## Acknowledgements

Many thanks to Audrey Roy and Daniel Greenfeld for writing [Two Scoops of django: Best Practices for Django 1.5](https://django.2scoops.org/). Many thanks to everyone who has posted helpful information on using Heroku with Django. Any clumsiness in my project is my fault, not theirs.
