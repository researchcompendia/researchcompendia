# tyler

intro paragraph here

I'm learning django best practices and following along with [Two Scoops of
django: Best Practices for Django 1.5](https://django.2scoops.org/) and their
recommended reading.

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

