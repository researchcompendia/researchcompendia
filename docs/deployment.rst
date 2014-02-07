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
   `researchcompendia-deployment <https://github.com/researchcompendia/researchcompendia-deployment>`_ is a work in progress for automating these steps.


Releasing
---------

Log in to the box that houses the site. Each release corresponds to a tag in
our repo. For a new release checkout the corresponding tag and create a new
virtualenv for the tag.  Edit /home/tyler/site/bin/environment.sh to update the
SITE_VERSION.  As the tyler user::

  cd /home/tyler/site
  source bin/environment.sh
  cd /home/tyler/site/tyler
  git checkout 1.0.1-b4
  mkvirtualenv 1.0.1-b4
  pip install -r requirements/production.txt


Check release notes for any required updates to environment variables, database
migrations, static files changes.

As a sudo user (not tyler) restart the app::

  sudo supervisorctl restart researchcompendia 

Tail the gunicorn log to make sure everything goes smoothly.::

  tail -f /home/tyler/site/logs/gunicorn_worker.log

Use `sudo htop` for a handy way to observe and control running processes.

.. Note:: fabric.py in the researchcompendia-deployment repo defines a `deploy`
   task that automates these steps. This is experimental.


Operations
----------

Logs for the webapp are here /home/tyler/site/logs. Logs are also streamed to
a `papertrail <https://papertrailapp.com/dashboard>`_ account and archived in s3 after a week.::

 logs
 ├── celery_worker.log         logs for celery and tasks
 ├── cron_checkdownloads.log   logs to see that the download link checker was called
 ├── gunicorn_supervisor.log   gunicorn/django console logs
 ├── log_files.yml             papertrail remote_syslog config file
 ├── tyler.access.log          nginx access log
 └── tyler.error.log           nginx error log

collectd is sending metrics to `graphite <https://162.242.230.222/>`_, nothing fancy yet.

Convenient packages like `htop` and `multitail` are installed.

Remote logging, the webapp, and celery are controled by supervisor. run `sudo supervisorctl status`
to see a list of statuses.::

 $ sudo supervisorctl status
 celery                           EXITED     Jan 16 11:21 PM
 remote_syslog                    RUNNING    pid 13411, uptime 1 day, 0:05:17
 researchcompendia                RUNNING    pid 13828, uptime 1 day, 0:01:17


Provisioning
------------

The site deployment and management is handled similarly to the recommendations
suggested in `Setting up Django with Nginx, Gunicorn, virtualenv, supervisor
and PostgreSQL
<http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/>`_
by Michal Karzynski.  Automated configuration is being worked on in the
`researchcompendia-deployment
<https://github.com/researchcompendia/researchcompendia-deployment>`_ repo.
This repo contains templates and scripts used to run the site.

To start provisioning a new system, create a new VM using your favorite method and platform.

As *root*, add your sudo user::

  adduser --ingroup sudo someuser

Now stop being root and become *someuser*. Log out of the box. Navigate to the
directory that contains the cloned researchcompendia-deployment. Let's consider the
case where you want to provision `staging` Run::

  fab staging provision

This task installs dependencies, installs postgresql and the site
database, and creates the researchcompendia user from which ResearchCompendia is run.


Installation Layout
:::::::::::::::::::

The provision task creates a directory layout organized in the following way::

  
  $ tree -L 2 site
  site
  ├── bin
  │   ├── celeryworker.sh
  │   ├── check_downloads.sh
  │   ├── environment.sh
  │   └── runserver.sh
  ├── logs
  │   ├── log_files.yml
  └── tyler

Until the deployment and configuration process is automated, there are manual
steps to go through for a first install and deployment.

* Obtain an `environment.sh` file
* Verify accuracy of `SITE_VERSION`
* activate the appropriate virtualenv, for example, if it is named `researchcompendia`
  you'd activate it by typing `workon researchcompendia`
* Set up the database::

    cd /home/tyler/site/
    source bin/environment.sh
    cd /home/tyler/site/tyler/companionpages
    ./manage.py syncdb --migrate
    ./manage.py loaddata fixtures/*

You may also want to create a superuser. createsuperuser::

    ./manage.py createsuperuser

Controlling researchcompendia
:::::::::::::::::::::::::::::

Once you've set up researchcompendia, update supervisor so that it launches the site::

  sudo supervisorctl reread
  sudo supervisorctl update
