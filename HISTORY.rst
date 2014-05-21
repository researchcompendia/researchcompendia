.. :changelog:

History
-------

1.3.0
+++++

1.3.0-b3 (2014-05-21)
#####################

* Updates requirements to upgrade from insecure versions


1.3.0-b2 (2014-05-19)
#####################

* This adds a sample Table of Contents view for the ASA Commons with the a list
  of results based on the request from the ASA group. Results cards for this type
  of browsing won't have abstract information. At the moment, they do not want 
  facets on the top level Table of Contents view. We can refine this in future iterations.
* With new browsing types of pages the pagination logic was getting repeated a
  lot so it has been factored out in to a separate template for DRY and also so
  that we have consistent pagination style.
* This adds a microformat to our header for rel-vcs as specified by https://joeyh.name/rfc/rel-vcs/

1.3.0-b1 (2014-05-12)
#####################

* Style changes for faceted searching and browsing

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
