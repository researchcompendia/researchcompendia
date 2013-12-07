.. _devsetup:

================================
Getting Started with Development
================================

Ready to contribute code? Here's how to set up `ResearchCompendia` for local development.

Getting Code
------------

1. Fork the `tyler` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_username_here/tyler.git
    $ cd tyler
    $ git remote add upstream https://github.com/researchcompendia/tyler.git

3. Install your local copy into a virtualenv. Here is one way to do it::

    $ cd tyler/
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements/local.txt

   You can also use `virtualenvwrapper
   <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ if you have it is
   installed. It is convenient, though not required.

4. Get help from someone to set up the environment variables for running locally.

   We can give you a .env file that works with foreman. We've tried to make it so that
   the django settings have some sensible defaults for running without environment variables,
   but not all of them have sensible defaults.

Making Changes
--------------

1. Make your changes.

   Now that you have the code, a virtualenv, and the proper environment variables, you are ready to make your changes locally.

2. Periodically update your branch from the parent repo. Use git rebase (not git merge)::

    $ git fetch upstream
    $ git rebase upstream/develop

You may want to do an `interactive rebase <https://help.github.com/articles/interactive-rebase>`_
in order to squash or fix small commits.

3. Check that your changes pass style check and tests::

    $ make test

4. Commit your changes and push your branch to up to your fork on GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes for #123"
    $ git push

Reviewing Changes
-----------------

Submit a pull request through the GitHub website to submit it for review. Before you submit
a pull request, check that it meets these guidelines:

  0. The pull request should be easy to review.
  1. The pull request should include tests
  2. Check https://travis-ci.org/researchcompendia/tyler/pull_requests
     and make sure that the tests pass
  3. If the pull request adds functionality, the docs and/or comments should be updated.
