============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given. 

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/runmycode/tyler/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Brainstorm Features
~~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for brainstorming discussions. Anything tagged
with "brainstorming" is open to discussion.

Review Code
~~~~~~~~~~~

Look through pull request and review the changes. Review code in our repository as well
and suggest improvements and alternatives.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Tyler could always use more documentation, whether as part of the 
official Tyler docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/runmycode/tyler/issues.


* If you are proposing a feature explain in detail how it would work.
* Keep the scope as narrow as possible, to make an issue easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `tyler` for local development.

1. Fork the `tyler` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/tyler.git

3. Install your local copy into a virtualenv.::

    $ cd tyler/
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements/local.txt

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
tests::

    $ flake8 companionpages
    $ companionpages/manage.py test

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests
2. Check https://travis-ci.org/runmycode/tyler/pull_requests
   and make sure that the tests pass
3. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
