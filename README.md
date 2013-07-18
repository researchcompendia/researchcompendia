# tyler

I'm learning django best practices and following along with [Two Scoops of
django: Best Practices for Django 1.5](https://django.2scoops.org/) and their
recommended reading.

I started out creating a skeleton of a project following their skel repo, but
this has started to diverge. I decided to flatten the settings and use environment
variables to get the effect of settings files for different environments.

Since this is an open learning exercise, I've blogged about some of the process
under the [django](http://codersquid.github.io/tag/django.html) tag.

## Working Environment

To set up a working environment,

* `git clone git@github.com:codersquid/tyler.git`
* `cd tyler`
* `virtualenv venv`
* `source venv/bin/acivate`

### Installation of Dependencies

Depending on where you are installing dependencies:

* In development:
    * `pip install -r requirements/local.txt`
* For production:
    * `pip install -r requirements.txt`

note: We install production requirements this way because many Platforms as
a Services expect a requirements.txt file in the root of projects.

## Acknowledgements

Many thanks to Audrey Roy and Daniel Greenfeld for writing [Two Scoops of django: Best Practices for Django 1.5](https://django.2scoops.org/). Any clumsiness in my project is my fault, not theirs.

