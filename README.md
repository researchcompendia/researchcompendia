# tyler

## Build Status

![current build status](https://travis-ci.org/codersquid/tyler.png?branch=master)

[build history](https://travis-ci.org/codersquid/tyler)

## Intro

This repo contains a skeleton Django project that is deployable on Heroku or on
a local or remote machine. Static files are served locally in DEBUG mode or via
S3 when deployed to Heroku and/or in non-DEBUG mode.

The Heroku instance is [RunMyAlpha](http://runmyalpha.herokuapp.com/). It only has one worker for now.


I've set up a [trello](https://trello.com/b/8KC8wAye/rmc) board and have also
created [issues](https://github.com/codersquid/tyler/issues) in the github tracker.
I'm trying out both tools to see which is most useful, I may find a tool to link them up
in case they both are. I wish there was a trello-like UI for the github tracker.

## Site Design

This is entirely in flux. Right now there are two empty apps, `results` and `status`.
There will be more, probably by the end of the day.

* `results`: this will stay empty until we get to the point where we want to show history pages with the results of runs
* `status`: this will stay empty until we get to the point where we want a site status page with status news, graphs, etc. actually, I should probably rip this out and make a static page and stick it on another webserver entirely? I'll figure that out.

## Working Environment

To set up a working environment,

* `git clone git@github.com:codersquid/tyler.git`
* `cd tyler`
* `virtualenv venv`
* `source venv/bin/acivate`
* `pip install -r requirements.txt`

You may need to define these environment variables to run this locally.

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
