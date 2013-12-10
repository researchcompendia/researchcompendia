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
corresponding tag and create a new virtualenv for the tag. As the tyler user::

  cd /home/tyler/site/tyler
  git checkout tags/1.0.0-beta4
  mkvirtualenv tyler_1.0.0-beta4
  pip install -r requirements/production.txt

Edit /home/tyler/site/bin/runserver.sh to change the VERSION.

Check release notes for any required updates to environment variables or any
migrations for the database. Review /home/tyler/site/bin/environment.sh for
accurate environment settings.

As a sudo user (not tyler) restart the app::

  sudo supervisorctl restart tyler

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

Create a server VM using your favorite method and platform.

As *root*, add your sudo user::

  adduser --ingroup sudo someuser

Now stop being root and become *someuser* from now on.

Add the tyler application user and group::

  sudo addgroup tyler
  sudo adduser --ingroup tyler tyler

You'll want to go through the steps of setting up ssh keys.


System Dependencies
:::::::::::::::::::

Install required package dependencies::

  sudo apt-get install python-dev \
    build-essential \
    curl \
    python-pip \
    nginx \
    libxslt1-dev \
    supervisor \
    git \
    postgresql \
    postgresql-server-dev-9.1

Install convenient package dependencies::

  sudo apt-get install vim \
    exuberant-ctags \
    multitail \
    install tmux \
    ack-grep

Install global python packages::

  sudo pip install virtualenvwrapper
  sudo pip install setproctitle # or just in a virtualenv?


Database
::::::::

Set up database as postgres::

  sudo su postgres -c 'createuser -S -D -R -w tyler'
  sudo su postgres -c 'createdb -w -O tyler tyler'

Add an entry to /etc/postgresql/9.1/main/pg_hba.conf,
*local   sameuser    all         ident*

restart postgres::

  sudo service postgresql restart


Directory Layout
::::::::::::::::

Create a directory layout organized in the following way::

 /home/tyler/
 site
 ├── bin
 │   ├── README
 │   └── runserver.sh
 ├── logs
 │   ├── gunicorn_supervisor.log
 │   ├── tyler.access.log
 │   └── tyler.error.log
 └── tyler

Configurations
::::::::::::::

Configuration files will be checked in to a repo, but for now I have
them in `this gist <https://gist.github.com/codersquid/7583630>`_.

* /etc/supervisor/conf.d/tyler.conf
* /etc/nginx/sites-available/researchcompendia

Once you link up researchcompendia in sites-enabled, restart nginx::

  sudo service nginx restart

Once you add a supervisor conf for tyler reload and update conf files::

  sudo supervisorctl reread
  sudo supervisorctl update


Heroku
------

Everything is different for running this on Heroku.  Heroku deployment has been
straightforward for the most part. I need to document how to check out a repo
and hook it up to our heroku env.  I've got `working notes
<https://github.com/researchcompendia/tyler/wiki/Development-environments>`_ in
the wiki.
