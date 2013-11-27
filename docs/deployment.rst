.. _deployment:


==========
Deployment
==========

This document section is completely in flux. The process being documented is not
fully formed. We will eventually have automation worked out. Right now this describes
a manual process.

Deploying new release on Debian
-------------------------------

For every new release we want to deploy fetch a specific tarball from github
for that version. Create a new virtualenv for that version.  Tar up the old
tyler directory in /home/tyler/site/tyler and rotate it out.  Untar the new
repo in to /home/tyler/site/tyler. cd in to the new tyler directory and run pip
install -r requirements/production.txt.  (then supervisor something something something)


Installing and Setup for Debian
-------------------------------

Recommended Conventions
```````````````````````

The site deployment and management is handled similarly to the recommendations
suggested in `Setting up Django with Nginx, Gunicorn, virtualenv, supervisor and PostgreSQL
<http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/>`_
by Michal Karzynski.

Convention Differences
::::::::::::::::::::::

There are some differences from Michal's recommended layout.  You can see the differences in
our runserver.sh script versus his gunicorn_start.sh script. Some difference are:

* $VERSION
* $VIRTUALENV
* using .django.sh
* binding

Right now the runserver.sh script and conf files are checked in to this 
`gist <https://gist.github.com/codersquid/7583630>`_. When we have things settled down,
this will be in our repo.


VERSION
'''''''

For each release, there will be a new virtualenv created specifically for that release.
The virtualenv name will follow the convention of tyler_$VERSION. We'll keep a number of
virtualenvs from old releases around until they need to be cleaned out.

VIRTUALENV
''''''''''

The blog post has virtualenvs being created in the site directory, but I prefer keeping 
virtualenvs organized following the conventions of virtualenvwrapper.

Using .django.sh
''''''''''''''''

Environment variables are set in this file, and get used by django for tailoring 
settings for our environments.

Reason: We are following the `12factor <http://12factor.net/>`_ application model (before I 
saw the fancy page, it was "I'm following the advice of some friends who deploy stuff
at the Chicago Tribune. Thanks Chicago Tribune friends!")

Setup and installation
``````````````````````
Recap: Until we have this documented in automated deployedment tools, I'm documenting this here.

Create a server VM.

Users
:::::

as root, add your sudo user::

  adduser --ingroup sudo someuser

as *someuser* 

Add your application user and group::

  sudo adduser --ingroup tyler tyler

You'll probably want to do ssh-keygen and set up authorized_keys as well. I also
set up an ssh key with github and checkout my dot files. This may or may not be
advised.


System Dependencies
:::::::::::::::::::

Install system dependencies::

  sudo apt-get install python-dev
  sudo apt-get install build-essential
  sudo apt-get install curl
  sudo apt-get install python-pip
  sudo apt-get install nginx
  sudo apt-get install libxslt1-dev
  sudo apt-get install supervisor
  sudo apt-get install git
  sudo apt-get install postgresql
  sudo apt-get install postgresql-server-dev-9.1

Install convenient packages::

  sudo apt-get install vim
  sudo apt-get install exuberant-ctags
  sudo apt-get install multitail
  sudo apt-get install tmux

Database
::::::::

Set up database::

  # make database for app user
  sudo su postgres -c 'createuser -S -D -R -w tyler'
  sudo su postgres -c 'createdb -w -O tyler tyler'
  # add the following to /etc/postgresql/9.1/main/pg_hba.conf
  #  local   sameuser    all         ident

Global python packages
::::::::::::::::::::::

Install global python packages::

  sudo pip install virtualenvwrapper
  sudo pip install setproctitle (or just in venv?)


Directory Layout
::::::::::::::::

How I layed out the directory for now::

 /home/tyler/
 |
 +-- site/
 |   |
 |   +-- bin/runserver.sh
 |   +-- logs/
 |   +-- media/
 |   +-- run/
 |   +-- static/
 |   +-- tyler/ django root
 |
 +-- venvs/ all the virtualenvs


Reminders
`````````

Supervisor
::::::::::

I'm new to supervisor, so I need some reminders here on where the supervisor config files go
and supervisor subcommands.

`/etc/supervisor/conf.d/tyler.conf`

If you have root you can check status, start, stop using the supervisorctl command.

example: `sudo supervisorctl status tyler`



Heroku
------

Heroku deployment has been straightforward for the most part. I need to document
how to check out a repo and hook it up to our heroku env.
I've got `working notes <https://github.com/researchcompendia/tyler/wiki/Development-environments>`_
in the wiki.
