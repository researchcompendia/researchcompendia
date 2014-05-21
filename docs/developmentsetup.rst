.. _devsetup:

================================
Getting Started with Development
================================

.. Note:: If you have just started, this may seem confusing, and that is okay.
   No one starts out understanding how to do all of this. Additionally, anything that is
   confusing is a bug in our docs. Please open an issue to let us know where we
   need to improve things.

Ready to contribute code? Here's how to set up `ResearchCompendia` for local
development.

Getting Code
------------

Fork the repository and check out your fork and add our repo as a remote::

   $ git clone https://github.com/YOURACCOUNT/researchcompendia.git
   $ cd researchcompendia
   $ git remote add parent https://github.com/researchcompendia/researchcompendia.git


Installing Dependencies
-----------------------

1. Install your local copy into a virtualenv. Here is one way to do it::

    $ cd researchcompendia/
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements/ci.txt

   You can also use `virtualenvwrapper
   <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ if you have it is
   installed. It is convenient, though not required.

2. Set up environment variables. Once you have the environment varialbes set up, you are ready to
   set up the database.

3. We use Postgres as our database backend. We haven't written docs to
   walk though setting up Postgres yet. If you are unfamiliar with this
   process, you could consider using sqlite locally event thought our
   preferences is to use postgres in all environments. If you'd like to use
   sqlite, set up your DATABASE_URL environment variable to have a path to 
   a file name that will hold your database. for example::

     'sqlite:////path/to/my/site/root/researchcompendia.db'


Setting up the Environment
--------------------------

These are the environment variables that are used in the site settings listed along with their defaults.
For any default that doesn't apply to you, make an environment variable with your preferred setting.

You are required to create SECRET_KEY environment variable.

If you use fabric to provision a vagrant box,
it will generate a SECRET_KEY for you.

  =================================  ===========================================================================
  Environment Variable               Default Setting
  =================================  ===========================================================================
  ADDTHIS_GA_TRACKER                 ''
  ADDTHIS_GA_TRACKING_ENABLED        False
  ADDTHIS_PUBID                      ''
  ADMINS                             compendia@example.com
  AWS_ACCESS_KEY_ID                  ''
  AWS_SECRET_ACCESS_KEY              ''
  AWS_STORAGE_BUCKET_NAME            compendiaexamplebucket
  DATABASE_URL                       postgres://:5432/researchcompendia
  DJANGO_BROKER_URL                  hamqp://guest:guest@localhost:5672//
  DJANGO_CELERY_DISABLE_RATE_LIMITS  True
  DJANGO_CELERY_RESULT_BACKEND       cache+memcached://127.0.0.1:11211/
  DJANGO_CELERY_RESULT_SERIALIZER    json
  DJANGO_CELERY_TASK_SERIALIZER      json
  DJANGO_CELERY_TIMEZONE             US/Central
  CROSSREF_PID                       ''
  DEBUG                              True
  DEFAULT_FILE_STORAGE               django.core.files.storage.FileSystemStorage
  DEFAULT_FROM_EMAIL                 compendia@example.com
  DISQUS_API_KEY                     'none'
  DISQUS_WEBSITE_SHORTNAME           researchcompendiaorg
  BONSAI_URL                         http://127.0.0.1:9200
  EMAIL_BACKEND                      django.core.mail.backends.console.EmailBackend
  GA_TRACKING_CODE                   ''
  MAILGUN_ACCESS_KEY                 ''
  MAILGUN_SERVER_NAME                ''
  MEDIA_ROOT                         normpath(join(PROJECT_ROOT, 'media'))
  MEDIA_URL                          if using the s3boto storages then '%s/media/' % S3_URL, otherwise /media/
  REMOTE_DEBUG                       False
  SECRET_KEY                         no default. will blow up if not set
  SITE_ID                            1
  STATICFILES_STORAGE                django.contrib.staticfiles.storage.StaticFilesStorage
  STATIC_ROOT                        normpath(join(PROJECT_ROOT, 'staticfiles'))
  STATIC_URL                         if using the s3boto storages then '%s/static/' % S3_URL, otherwise /static/
  =================================  ===========================================================================
  
Setting up the Database
-----------------------

Set up the database by running::

   $ cd companionpages
   $ ./manage.py syncdb --migrate
   $ ./manage.py loaddata fixtures/*


Launching ResearchCompendia
---------------------------

Once the database is set up, you can start the app::

    $ ./manage.py runserver

Or perhaps you would like to have detailed stacktraces and messages::

    $ ./manage.py runserver --traceback -v 3 

Making Changes
--------------

Now that you have the code, a virtualenv, and the proper environment variables, you are ready to make your changes locally.

1. Make a topic branch for your changes. For example, if you wanted to add twitter logins to the site, you could make a branch named *twitterlogin*::

   $ git checkout -b twitterlogin


2. Periodically update your branch from the parent develop branch. Use git rebase (not git merge)::

    $ git fetch parent
    $ git rebase parent/develop

   We prefer a pull request with one commit rather than many small commits.
   To avoid making a request with many commits, you can do an `interactive rebase
   <https://help.github.com/articles/interactive-rebase>`_ and use fixup.::

    $ git rebase -i parent/develop

3. Check that your changes pass style check and automated tests::

    $ make test

4. Demonstrate your changes. It can be helpful to share work you are running locally from your own machine so that other people can help test.  `PageKite <https://pagekite.net/>`_ is a free/libre open source software project that can do this for you. This `QuickStart <http://pagekite.net/support/quickstart/>`_ shows how.

5. Commit your changes and push your branch to up to your fork on GitHub.::

    $ git add .
    $ git commit -m "Adds twitter login for #123"
    $ git push origin twitterlogin

Now you are ready to make a pull request.

Reviewing Changes
-----------------

Submit a pull request through the GitHub website to submit it for review.
Before you submit a pull request, check that it meets these guidelines:

  0. The pull request should be easy to review.
  1. The pull request should include tests
  2. Check https://travis-ci.org/researchcompendia/researchcompendia/pull_requests
     and make sure that the tests pass
  3. If the pull request adds functionality, the docs and/or comments should be updated.


Trying out Vagrant
------------------

.. Note:: This section is for developers who have experience with Vagrant and Fabric

If you want to use Vagrant clone the `researchcompendia-deployment
<https://github.com/researchcompendia/researchcompendia-deployment>`_ repo. It
contains fabric files and a Vagrantfile that pulls down a debian wheezy VM from
vagrantcound::

    $ git clone https://github.com/researchcompendia/researchcompendia-deployment.git
    $ cd researchcompendia-deployment
    $ vagrant up
    $ fab vagrant provision

Provision is not idempotent, so running it twice will probably fail in interesting ways.
If you want to start over need to run `vagrant destroy` first.

Provision will set up the vagrant box in the same way that a production box is set up.
