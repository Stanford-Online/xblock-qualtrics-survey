Qualtrics Survey
==================

XBlock to ease linking to Qualtrics surveys.

|badge-ci|
|badge-coveralls|

The tool makes it easy for instructors to link to a Qualtrics survey
from within their course.

|image-lms-view-normal|


Installation
------------


System Administrator
~~~~~~~~~~~~~~~~~~~~

To install the XBlock on your platform,
add the following to your `requirements.txt` file:

    xblock-qualtrics-survey

You'll also need to add this to your `INSTALLED_APPS`:

    qualtricssurvey


Course Staff
~~~~~~~~~~~~

To install the XBlock in your course,
access your `Advanced Module List`:

    Settings -> Advanced Settings -> Advanced Module List

|image-cms-settings-menu|

and add the following:

    qualtricssurvey

|image-cms-advanced-module-list|


Use
---


Course Staff
~~~~~~~~~~~~

To add a Qualtrics Survey link to your course:

- go to a unit in Studio
- select "Qualtrics Survey" from the Advanced Components menu

|image-cms-add|

You can now edit and preview the new component.

|image-cms-view|

Using the Studio editor, you can edit the following fields:

- display name
- survey id
- university
- link text
- message
- parameter name for userid

Note: If you plan to make use of the "Param Name" field to store User ID
data, you will need to configure your Qualtrics surveys to in turn
collect that data on Qualtrics’ end.

|image-cms-editor-1|
|image-cms-editor-2|


Participants
~~~~~~~~~~~~

|image-lms-view-normal|

Students click on a link within the unit and this takes them to the survey.


.. |badge-coveralls| image:: https://coveralls.io/repos/github/Stanford-Online/xblock-qualtrics-survey/badge.svg?branch=master
   :target: https://coveralls.io/github/Stanford-Online/xblock-qualtrics-survey?branch=master
.. |badge-ci| image:: https://github.com/openedx/xblock-qualtrics-survey/workflows/Python%20CI/badge.svg?branch=master
   :target: https://github.com/openedx/xblock-qualtrics-survey/actions?query=workflow%3A%22Python+CI%22
.. |image-cms-add| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/cms-add.png
   :width: 100%
.. |image-cms-advanced-module-list| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/cms-advanced-module-list.png
   :width: 100%
.. |image-cms-editor-1| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/cms-editor-1.png
   :width: 100%
.. |image-cms-editor-2| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/cms-editor-2.png
   :width: 100%
.. |image-cms-settings-menu| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/cms-settings-menu.png
   :width: 100%
.. |image-cms-view| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/cms-view.png
   :width: 100%
.. |image-lms-view-normal| image:: https://s3-us-west-1.amazonaws.com/stanford-openedx-docs/xblocks/qualtrics-survey/static/images/lms-view-normal.png
   :width: 100%
