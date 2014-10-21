# Qualtrics Survey
Xbock for creating a Qualtrics survey.

## TODO List:
- [ ] Write tests
- [ ] Update the `student_view`
    - [ ] `./qualtricssurvey/private/view.html`
        - Add content to `<div class="qualtricssurvey_block"></div>` element
    - [ ] `./qualtricssurvey/private/view.js`
        - Add logic to `QualtricsSurveyView` function
    - [ ] `./qualtricssurvey/private/view.less`
        - Add styles to `.qualtricssurvey_block { }` block
    - [ ] `./qualtricssurvey/qualtricssurvey.py`
        - Add back-end logic to `student_view` method
- [ ] Update the `studio_view`
    - [ ] `./qualtricssurvey/private/edit.html`
        - Add `<LI>` entries to `<ul class="list-input settings-list">` for each new field
    - [ ] `./qualtricssurvey/private/edit.js`
        - Add entry for each field to `QualtricsSurveyEdit
    - [ ] `./qualtricssurvey/private/edit.less`
        - Add styles to `.qualtricssurvey_edit { }` block (if needed)
    - [ ] `./qualtricssurvey/qualtricssurvey.py`
        - Add entry for each field to ``
- [ ] Update package metadata
    - [ ] `./package.json`
        - https://www.npmjs.org/doc/files/package.json.html
    - [ ] `./setup.py`
        - https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
- [ ] Update `./Gruntfile.js`
    - http://gruntjs.com/getting-started
- [ ] Update `./README.markdown`
- [ ] Write documentation
- [ ] Publish on PyPi
