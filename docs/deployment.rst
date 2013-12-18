.. _deployment:

==========
Deployment
==========

.. Note:: If you are not a core developer you likely do not need these instructions.
   These are instructions for production deployment. You may be looking for:
   :ref:`devsetup`

.. Warning:: This document section is completely in flux. The process being
   documented is not fully formed. We will have automation worked out and
   instructions for different platforms and environments, but for now this
   describes a manual process on a debian server for a production environment.

Releasing
---------

Each release corresponds to a tag in our repo. For a new release checkout the
corresponding tag and create a new virtualenv for the tag. As the researchcompendia user::

  cd /home/researchcompendia/site/researchcompendia
  git checkout tags/1.0.0-beta4
  mkvirtualenv researchcompendia_1.0.0-beta4
  pip install -r requirements/production.txt

Edit /home/researchcompendia/site/bin/runserver.sh to change the VERSION.

Check release notes for any required updates to environment variables or any
migrations for the database. Review /home/researchcompendia/site/bin/environment.sh for
accurate environment settings.

As a sudo user (not researchcompendia) restart the app::

  sudo supervisorctl restart researchcompendia

Configuration
-------------

The site deployment and management is handled similarly to the recommendations
suggested in `Setting up Django with Nginx, Gunicorn, virtualenv, supervisor and PostgreSQL
<http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/>`_
by Michal Karzynski.

There are some differences from Michal's recommended layout.  You can see the
differences in our `runserver.sh
<https://gist.github.com/codersquid/7583630#file-runserver-sh>`_ script versus
his gunicorn_start.sh script. Some difference are:

* $VERSION
* $VIRTUALENV
* environment.sh

Right now the runserver.sh script and conf files are checked in to this `gist
<https://gist.github.com/codersquid/7583630>`_. When we have things settled
down, thise will be in our repo.

Environment variables are set in environment.sh file, and get used by django
for tailoring settings for our environments.  Reason: We are following the
`12factor <http://12factor.net/>`_ application model (before I saw the fancy
page, it was "I'm following the advice of some friends who deploy stuff at the
Chicago Tribune. Thanks Chicago Tribune friends!") Later we might use jezdez's
`envdir <https://github.com/jezdez/envdir>`_.  I've been trying it out locally.



Installation
------------

Create a new VM using your favorite method and platform.

As *root*, add your sudo user::

  adduser --ingroup sudo someuser

Now stop being root and become *someuser* from now on.


Run `bootstrap.sh
<https://github.com/researchcompendia/researchcompendia/blob/develop/bootstrap.sh>`_ as
sudo.  This script will install dependencies, set up postgresql and the site
database, and create the researchcompendia user from which ResearchCompendia is run.

Installation Layout
:::::::::::::::::::

The bootstrap.sh script create a directory layout organized in the following way::

 /home/researchcompendia/
 site
 ├── bin
 │   ├── README
 │   └── runserver.sh
 ├── logs
 │   ├── gunicorn_supervisor.log
 │   ├── researchcompendia.access.log
 │   └── researchcompendia.error.log
 └── researchcompendia

Until the deployment and configuration process is automated, there are manual
steps to go through for a first install and deployment.

* Obtain `environment.sh` and copy it to to `/home/researchcompendia/bin/`
* Verify accuracy of `VERSION` in `runserver.sh`.
* activate the appropriate virtualenv, for example, if it is named `researchcompendia`
  you'd activate it by typing `workon researchcompendia`

.. warning:: There is an issue that requires apps to be migrated explicitely versus calling `./manage.py migrate`.

* Set up the database::

    source /home/researchcompendia/site/bin/environment.sh
    cd /home/researchcompendia/site/researchcompendia/companionpages
    ./manage.py syncdb
    ./manage.py loaddata fixtures/*
    ./manage.py migrate taggit
    ./manage.py migrate users
    ./manage.py migrate home
    ./manage.py migrate compendia
    ./manage.py migrate allauth.socialaccount


Controlling researchcompendia
:::::::::::::::::::::::::::::

Once you've set researchcompendia, update supervisor so that it can launch the site::

  sudo supervisorctl reread
  sudo supervisorctl update


Heroku
------

Everything is different for running this on Heroku.  Heroku deployment has been
straightforward for the most part. I need to document how to check out a repo
and hook it up to our heroku env.  I've got `working notes
<https://github.com/researchcompendia/researchcompendia/wiki/Development-environments>`_ in
the wiki.
