===============================
Tyler
===============================

.. image:: https://travis-ci.org/researchcompendia/tyler.png?branch=master
        :target: https://travis-ci.org/researchcompendia/tyler

A proof of concept for a research compendia webapp.

Introduction and Goals
----------------------

What are *research compendia*?

Gentleman and Temple Lang [#]_ presented the concept of a compendium as a collection of
everything that has gone towards the work of a research publication. This idea reaches
back towards the Knuth's concept of literate programming but overlayed with reproducibility concerns.

The application has the following goals.

* We want to make it possible to collect all of the writing, code and data
  in to an archivable form that represents what was presented at the time
  of a publication or at any one point in time.
* We want to provide a way for users to run compendia in non-trivial ways.
* We want compendia to be re-mixable.
* We want to help researchers manage their research in a way that makes it mixable and executable.


If you are a programmer, you may find yourself thinking that some of these goals remind you of
a continuous integration and build system. And yes, in some sense the goal with this
prototype is to create a continuous integrations system for computational research.

Project milestones are loosely organized on our `planning wiki page <https://github.com/researchcompendia/tyler/wiki/planning-scratchpads>`_.

Project Structure
-----------------

This is a django project with the following structure.

* `home`: this handles the landing page, faq, and similar concerns that don't call for separate apps.
* `users`: this handles users and profiles by using django-allauth and cookiecutter-django's user template
* `compendia`: this handles the archiving and representation of a compendium.
* `lib`: this holds code that does not call for an app
* `api`: this handles our service apis.

Resources
---------

* Free software: `MIT License <http://opensource.org/licenses/MIT>`_
* Technical Documentation: http://tyler.rtfd.org
* Issue tracker: https://github.com/researchcompendia/tyler/issues
* Issue kanban: https://huboard.com/researchcompendia/tyler
* Wiki: https://github.com/researchcompendia/tyler/wiki
* IRC: #hackingscience on freenode.net

Development Environments
++++++++++++++++++++++++
* Beta http://researchcompendia.org
* Pre-prod: http://preprod-researchcompendia.herokuapp.com

Acknowledgements
----------------

Make a separate acknowledgements page?

References
----------

.. [#] Gentleman, Robert, and Duncan Temple Lang. 2007. “Statistical Analyses and Reproducible Research.” Journal of Computational and Graphical Statistics 16 (1): 1–23. doi:10.1198/106186007X178663. http://www.tandfonline.com/doi/abs/10.1198/106186007X178663.
