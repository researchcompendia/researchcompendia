.. _deployment:

==========
Deployment
==========

.. Note:: If you are not a core developer you likely do not need these instructions.
   These are instructions for production deployment. You may be looking for:
   :ref:`devsetup`

.. Warning:: This process is in flux and not fully automated.


Initial Setup
-------------

Clone the `researchcompendia-deployment <https://github.com/researchcompendia/researchcompendia-deployment>`_ repo::

    $ git clone https://github.com/researchcompendia/researchcompendia-deployment.git
    $ cd researchcompendia-deployment
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt


The top of the fabric.py file has settings for hostnames, port numbers, etc.
Check these to verify that they apply to you. If they do not, change them as
appropriate.  Each fabric command should be prefaced with the name of the
environment, `dev`, `staging`, `prod`, `vagrant` are available environments. If
this is the first time you are setting up a box, run the provision task. This
example provisions staging::

    (venv)$ fab staging provision

Until the deployment and configuration process completely automated, there are
manual steps to go through for a first install and deployment.  You'll want to
create a django superuser. Log in to the box, sudo su tyler, source the environment
variables, run the createsuperuser command::

    ./manage.py createsuperuser

Creating A Release
------------------

Releases are created with the `git flow release` subcommands (part of `git-flow
<http://danielkummer.github.io/git-flow-cheatsheet/>`_).

Version numbers: We use a `semantic versioning <http://semver.org/>`_ scheme.

All of the changes you want to go in to a release should be in the `development`
branch. Once everything is there run (the version for this example is 1.0.0)::

    $ git flow release start 1.0.0

Once you've started a release, edit the HISTORY.rst file and bump the version in __init__.py and commit
the changes. Then run::

    $ git flow release finish 1.0.0

This will merge everything in develop to master and create a tag for you. Once that is done, you need to
push the changes::

    $ git checkout master
    $ git push
    $ git push --tags
    $ git checkout develop
    $ git push


Deploying a Release
-------------------

Check release notes for any required updates to environment variables, database
migrations, static files changes. Activate your researchcompendia-deployment
virtualenv and run the deploy command::

    (venv)$ fab staging deploy:1.0.0

That command is for the simplest case of a change. It doesn't migrate the database, for example.
There is a fab command for that, `migrate`


Miscellanea
-----------

Convenient packages like `htop` and `multitail` are installed.
Use `sudo htop` for a handy way to observe and control running processes.

The provision task creates a directory layout in the tyler user's home directory organized in the following way::

  
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

Logs for nginx, celery, gunicorn, supervisor, cron, django are in the logs/ directory.::

 logs
 ├── celery_worker.log         logs for celery and tasks
 ├── cron_checkdownloads.log   logs to see that the download link checker was called
 ├── gunicorn_supervisor.log   gunicorn/django console logs
 ├── log_files.yml             papertrail remote_syslog config file
 ├── tyler.access.log          nginx access log
 └── tyler.error.log           nginx error log


Remote logging, the webapp, and celery are controled by supervisor. run `sudo supervisorctl status`
to see a list of statuses.::

 $ sudo supervisorctl status
 celery                           EXITED     Jan 16 11:21 PM
 remote_syslog                    RUNNING    pid 13411, uptime 1 day, 0:05:17
 researchcompendia                RUNNING    pid 13828, uptime 1 day, 0:01:17
