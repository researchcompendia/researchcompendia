.. :changelog:

History
-------

1.1.1 (2014-03-16)
++++++++++++++++++

* First pull request from an external contributor! `#168 <https://github.com/researchcompendia/researchcompendia/pull/168>`_ fixes two typos in the FAQ. Thanks `@benmarwick <https://github.com/benmarwick>`_.


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

* We now tag things with a custom tag class.
* We've got some preliminary vagrant and boostrap scripts to allow people to stand up and deploy a researchcompendia site on their own vm.



1.0.0-beta6
+++++++++++

May docs changes

1.0.0-beta5
+++++++++++

Removed title from form message due to unicode error `#120 <https://github.com/researchcompendia/researchcompendia/issues/120>`_

1.0.0-beta4 (2013-12-09)
++++++++++++++++++++++++

Works around known issue `#74 <https://github.com/researchcompendia/researchcompendia/issues/74>`_
"getting ImproperlyConfigured: No URL to redirect to during a compendia update"


1.0.0-beta3 (2013-12-07)
++++++++++++++++++++++++

Changes
#######

* added DOI autocomplete to Create page `#43 <https://github.com/researchcompendia/researchcompendia/issues/43>`_

Minor Changes
#############

* Added information about fetch and rebase to the developer docs.

1.0.0-beta2 (2013-12-02)
++++++++++++++++++++++++

Minor Changes
#############

* Moved About, Partners, and Developers pages from flatpages to templates
* Template changed to make side navs fixed on About and Partners

Bug fixes
#########

* Fixes for broken download links on compendia index

1.0.0-beta1 (2013-11-27)
++++++++++++++++++++++++

Changes
#######

* Simple search over authors, title, abstract
* Faq page template changes
* Faq admin allows for ordering of questions


1.0.0-beta0 (2013-11-19)
++++++++++++++++++++++++

Changes
#######

* User page now has tabs for Profile, Compendia (if user has any), and Settings.

Bug fixes
#########

* added link to change password in user settings `#75 <https://github.com/researchcompendia/researchcompendia/issues/75>`_


1.0.0-beta (2013-11-11)
++++++++++++++++++++++++

* Many more template changes
* Site is starting to settle down

1.0.0-alpha (2013-10-24)
++++++++++++++++++++++++

* Simplified creation form
* Added admin action to flip items from draft to active
* Many template changes

1.0.0-alpha (2013-10-05)
++++++++++++++++++++++++

* Many stylistic changes
* Started using semantic versioning

0.11.0 (2013-09-17)
+++++++++++++++++++

* First release with docs
