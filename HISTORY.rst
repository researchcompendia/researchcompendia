.. :changelog:

History
-------

1.0.1-b9 (2014-02-16)
+++++++++++++++++++++

* Github and persona logins


1.0.1-b8 (2014-02-14)
+++++++++++++++++++++

* Adds fixtures for flatblocks for the text on the front page and the cite-me reminder.
* Front page explanation is now editable in the admin
* Fixes typos in faq


1.0.1-b7 (2014-02-04)
+++++++++++++++++++++

* Added cite-me display and dialog for journals `#60 <https://github.com/researchcompendia/researchcompendia/issues/60>`_
* Added additional fields for journals to the create and update compendia pages


1.0.1-b6 (2014-01-17)
++++++++++++++++++++++++

* Added Resources page and navbar link


1.0.1-b5 (2014-01-22)
++++++++++++++++++++++++

* Resources is now a flatpage


1.0.1-b4 (2014-01-17)
++++++++++++++++++++++++

* Removing Resources link from nav, it was added by accident

1.0.1-b3 (2014-01-16)
++++++++++++++++++++++++

* Allows markdown in compendia abstracts

1.0.1-b2 (2014-01-15)
++++++++++++++++++++++++

* Minor but useful settings changes for logging
* Added "dark" /resources url to serve as example for a mostly static page


1.0.1-b1 (2014-01-07)
++++++++++++++++++++++++

* Minor change to add help text indicating file upload size limitation in creation form

1.0.1-beta0 (2013-12-23)
++++++++++++++++++++++++

* Users can no longer select a different compendia owner


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
