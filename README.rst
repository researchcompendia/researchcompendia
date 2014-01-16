===============================
ResearchCompendia
===============================

.. image:: https://travis-ci.org/researchcompendia/researchcompendia.png?branch=master
        :target: https://travis-ci.org/researchcompendia/researchcompendia

A proof of concept for a research compendia webapp.

Introduction and Goals
----------------------

This is a project to allow scientists to create research compendium [#]_ comprising all
relevant narrative, code, and data to make their research truly reproducible.
Our goal is allow and teach researchers to document the computational portions of
their research methods as thoroughly as they would document a tabletop
experiment. We want our tools to fulfill these goals:

The application has the following goals.

* We will make it possible to archive all of the data, codes, documentation, parameters,
  and environmental settings linked with published research in a versioned form.
* We will support the verification and validation processes by providing for the execution
  of shared code and the visualization of results.
* We want to help and encourage researchers to manage their research in a way that makes it mixable and executable.
* Most of all we wish to make these tools heavily automated, and easy to access and
  utilize to lessen the exertion required from already overburdened academic researchers in the process of
  publishing fully reproducible work.


Imagine if all the materials in a research project could be continuously
packaged and deployed with no snags preventing use and refinement by anyone. We
could help make research accessible to everyone.

Project milestones are loosely organized on our `planning wiki page <https://github.com/researchcompendia/researchcompendia/wiki/planning-scratchpads>`_.

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
* Technical Documentation: http://tyler.readthedocs.org/en/latest/
* Issue tracker: https://github.com/researchcompendia/researchcompendia/issues
* Issue kanban: https://huboard.com/researchcompendia/researchcompendia
* Wiki: https://github.com/researchcompendia/researchcompendia/wiki
* IRC: #hackingscience on freenode.net

Development Environments
++++++++++++++++++++++++
* http://researchcompendia.org
* Pre-prod: http://labs.researchcompendia.org

Acknowledgements
----------------

Make a separate acknowledgements page?

References
----------

.. [#] Gentleman, Robert, and Duncan Temple Lang. 2007. “Statistical Analyses and Reproducible Research.” Journal of Computational and Graphical Statistics 16 (1): 1–23. doi:10.1198/106186007X178663. http://www.tandfonline.com/doi/abs/10.1198/106186007X178663.
