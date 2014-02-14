.. _devsetup:

================================
Getting Started with Development
================================

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

2. Get help from someone to set up the environment variables for running
   locally. Once you have the environment varialbes set up, you are ready to
   set up the database.

3. We use Postgres as our database backend. We haven't written docs to
   walk though setting up Postgres yet. If you are unfamiliar with this
   process, you could consider using sqlite locally event thought our
   preferences is to use postgres in all environments.
   

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

Vagrant is not completely supported yet, but if you would like to try out
what I've done so far, check out the `researchcompendia-deployment <https://github.com/researchcompendia/researchcompendia-deploymentrepo>`_ and run `vagrant up`. This will
pull down a debian wheezy VM from puppetlabs if you don't already have it
and launch the VM::

    $ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    [default] Clearing any previously set forwarded ports...
    [default] Creating shared folders metadata...
    [default] Clearing any previously set network interfaces...
    [default] Preparing network interfaces based on configuration...
    [default] Forwarding ports...
    [default] -- 22 => 2222 (adapter 1)
    [default] -- 80 => 8000 (adapter 1)
    [default] Booting VM...
    [default] Waiting for machine to boot. This may take a few minutes...
    [default] Machine booted and ready!
    [default] Mounting shared folders...
    [default] -- /vagrant

Once the VM is running, you can login::

    $ vagrant ssh
    Linux debian-70rc1-x64-vbox4210 3.2.0-4-amd64 #1 SMP Debian 3.2.35-2 x86_64

    The programs included with the Debian GNU/Linux system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Sun Dec 15 20:20:08 2013 from 10.0.2.2

Read through the fabfile.py script and take a look at the `provision` task. This task
provisions a box to install all the dependencies and prepares a box for site deployment.
