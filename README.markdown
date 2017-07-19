# Qualtrics Survey
Xblock for creating a Qualtrics survey.

This package provides a Xblock for use with the Edx platform that makes it
easy to link to a Qualtrics survey from your course.

Instructors define the following paramters in Studio:
- display name
- survey id
- university
- link text
- message
- parameter name for userid

Students click on a link within the unit and this takes them to the survey.



# Installation
- Add the xblock to your requirements/edx/github.text file
  e.g. -e git+https://github.com/Stanford-Online/xblock-qualtrics-survey@cfb793db182b60281875b83b53a98640d740ebcf#egg=xblock-qualtrics-survey

- In Studio Settings/Advanced Settings add the xblock to the Advanced Module List.
  e.g. "qualtricssurvey"

Now, when you create a component "Qualtrics Survey" should appear in the Advanced Component List.

