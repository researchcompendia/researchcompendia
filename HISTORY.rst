.. :changelog:

History
-------

1.3.1 (2014-06-03)
++++++++++++++++++

* Fixes `#196 <https://github.com/researchcompendia/researchcompendia/issues/196>`_, /search/ without query parameters caused a 500.


1.3.0
+++++

* Adds a Demos page where we can list ongoing demos. Currently we have a Table of Contents
  demo and some executability demos.
* The demo Table of Contents demo allows for an admin to generate a table of contents based on
  entries that categorize compendia types. The current demo shows a result card style with no
  stripped down informationc ompared to the main site result card style.
* Adds facets based on compendium type and primary research fields. These are stackable in the url, but
  the UI only drills down via links for now.
* Upgrades insecure requirements. Started tracking requirements via the https://requires.io service.
* Adds microformat to our header for rel-vcs as specified by https://joeyh.name/rfc/rel-vcs/
* template refactoring -- pulled out some browse, facet, and pagination code in to separate files to be
  included in other templates. DRY
* minor style changes


1.2.1 (2014-05-12)
++++++++++++++++++

New Features and content
########################

* Facetted search based on primary research field and compendium type `#184 <https://github.com/researchcompendia/researchcompendia/pull/184>`_
* Started `Project Structure <https://github.com/researchcompendia/researchcompendia/blob/develop/docs/project.rst>`_ docs

Fixes
#####

* User detail page broken due to old url pattern `#182 <https://github.com/researchcompendia/researchcompendia/issues/182>`_

1.2.0 (2014-04-14)
++++++++++++++++++

* First pull request from an external contributor! `#168 <https://github.com/researchcompendia/researchcompendia/pull/168>`_ fixes two typos in the FAQ. Thanks `@benmarwick <https://github.com/benmarwick>`_.
* First iteration with execution with some limited ability to do parameter passing, with execution history
* DOI minting for data and code


1.1.0 (2014-03-06)
+++++++++++++++++++++

New features and content
########################

* Users can log in with Github and Persona
* Citations: compendia pages list citation information and users are reminded to cite code and data
  when they go to download code or data. `#60 <https://github.com/researchcompendia/researchcompendia/issues/60>`_
* Additional fields are auto-completed with the DOI auto-fill
* Added a Resources page with information about reproducible science and research compendia
* Compendia abstracts can use markdown

Fixes
#####

* Citations show et. al. for papers with more than 5 authors `#161 <https://github.com/researchcompendia/researchcompendia/issues/161>`_
* Styling fixes for side navigation


1.0.0 (2013-12-18)
++++++++++++++++++

First talk! Now that we've had the first talk about this, let's have 1.0.0!

Not a lot of user-facing changes for this release. We've Renamed project ResearchCompendia
from the pre-release *tyler* name, and renamed the repo to go with that.

* We have tagging on creation, but tags are not yet used for search and browsing.
* We have simple text search that searches through authors, title, abstract
* We have a simple compendium creation form with DOI autocompletition.
* We have some prelimary developer docs that discuss contributions and development.
* We have user profile pages so that users can view a list of their compendia. 
