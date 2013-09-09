# tyler


![current build status](https://travis-ci.org/runmycode/tyler.png?branch=master)
[build history](https://travis-ci.org/runmycode/tyler)

## Intro

This repo contains a proof of concept for a Django-based RunMyCode site.

The heroku instance for this proof of concept is at
[rose-tyler-alpha](http://rose-tyler-alpha.herokuapp.com/)

* [issue tracker](https://github.com/codersquid/tyler/issues)
* kanban board [trello](https://trello.com/b/8KC8wAye/rmc)


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


## Site Design

This is entirely in flux but I want to at least splat some links here

#### custom apps

* `home`: this handles the landing page, faq, and similar concerns that don't call for separate apps.
* `members`: this handles member profiles. It's very spare for now.
* `news`: this handles short twitteresque announcements and news. I'll probably dump this app. I just exists to demonstrate quickly something askin to newsfeed on the main page.
* `status`: this will stay empty until we get to the point where we want a site status page with status news, graphs, etc. actually, I should probably rip this out and make a static page and stick it on another webserver entirely? I'll figure that out.
* `supportingmaterials`: this handles pages for article companion sites with code and data. It's spare for now.

#### third party docs

* [django-model-utils](https://django-model-utils.readthedocs.org/en/latest/)
* [django-storages, s3](http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html) see also heroku docs on [django static assets](https://devcenter.heroku.com/articles/django-assets)
* [django-profiles](https://bitbucket.org/ubernostrum/django-profiles)
   * waiting on [pull request](https://bitbucket.org/ubernostrum/django-profiles/pull-request/6/replaced-profile_list-view-with-a-class/diff) which is why requirements point directly to fcurella's zip
   * [blog post, slightly outdated but helpful](http://birdhouse.org/blog/2009/06/27/django-profiles/)
* [django-registration](https://bitbucket.org/ubernostrum/django-registration) and a [blog post](http://www.michelepasin.org/blog/2011/01/14/setting-up-django-registration/)
* [django-envelope](http://django-envelope.readthedocs.org/en/latest/index.html)
* [boostrap](http://getbootstrap.com/)
* [fontawesome](http://fontawesome.io/)
* heroku has good docs and a helpful [discussion](https://discussion.heroku.com/) forum.
* my bookmarks tagged with [tyler](https://pinboard.in/u:sky/t:tyler/) that includes the above and more

### evaluate for future use

* [django-admin2](https://github.com/pydanny/django-admin2): we'd get a more customizable admin with class based views rather than the oldschool ones.
* [zinnia blog app](http://docs.django-blog-zinnia.com/en/latest/): we wouldn't write something like the newsfeed functionality from scratch if we can evaluate whether the blog excerpt functionality in this behaves nicely... and then as a benefit we'd have a full featured blog that we could use for posts on the news/blog page.
* accounts/login
   * [django-browserid](https://github.com/mozilla/django-browserid): email based registration and accounts using mozilla persona.
   * [django-socialauth](http://django-social-auth.readthedocs.org/en/latest/index.html): accounts via github, google, twitter, facebook, and so on and so forth


## tools

* [contrast ratios testing ](http://leaverou.github.io/contrast-ratio/)
* [colorzilla gradient editor](http://www.colorzilla.com/gradient-editor/)
* [browser comparison for css gradient support](http://caniuse.com/css-gradients)
* [css sprite discussion](http://css-tricks.com/css-sprites/)
* [discussion on css3 gradients](http://css-tricks.com/css3-gradients/)
* [color scheme designer](http://www.colorschemedesigner.com/)
* [compress png images](http://tinypng.org/)
* [spriteme](http://spriteme.org/)
* [mobile phone emulator](http://www.mobilephoneemulator.com/)
* [device emulators](http://mattkersley.com/responsive/)


## Acknowledgements

Many thanks to Audrey Roy and Daniel Greenfeld for writing [Two Scoops of django: Best Practices for Django 1.5](https://django.2scoops.org/). Many thanks to everyone who has posted helpful information on using Heroku with Django. Any clumsiness in my project is my fault, not theirs.

## Random stuff

tyler is named after Rose Tyler, who was a companion of The Doctor. Django is named after a person too.
