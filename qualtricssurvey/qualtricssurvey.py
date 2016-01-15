"""
This is the core logic for the Qualtrics Survey
"""
import os
import pkg_resources, cgi

from django.utils.translation import ugettext as _

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

class QualtricsSurvey(StudioEditableXBlockMixin, XBlock):
    """
    Xblock for creating a Qualtrics survey.
    """
    display_name = String(
        display_name=_('Display Name:'),
        default=_('Qualtrics Survey'),
        scope=Scope.settings,
        help=_('This name appears in the horizontal navigation at the top of the page.'),
    )
    survey_id = String(
        display_name=_('Survey ID:'),
        default=_('Enter your survey ID here.'),
        scope=Scope.settings,
        help=_(
            'This is the ID that Qualtrics uses for the survey, which can '
            'include numbers and letters, and should be entered in the '
            'following format: SV_###############'
        ),
    )
    your_university = String(
        display_name=_('Your University:'),
        default=_('stanford'),
        scope=Scope.settings,
        help=_('This is the name of your university.'),
    )                       
    link_text = String(
        display_name=_('Link Text:'),
        default=_('click here'),
        scope=Scope.settings,
        help=_('This is the text that will link to your survey.'),
    )
    param_name = String(
        display_name=_('Param Name:'),
        default=_('a'),
        scope=Scope.settings,
        help=_('This is the name for the User ID parameter in the url. If blank, User ID is ommitted from the url.'),
    )
    editable_fields = ('display_name', 'survey_id', 'your_university', 'link_text', 'param_name')

    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """

        display_name = self.display_name
        survey_id = self.survey_id
        your_university = self.your_university
        link_text = self.link_text
        param_name = self.param_name

        anon_user_id = self.xmodule_runtime.anonymous_student_id

        # %%PARAM%% substitution only works in HTML components
        # so it has to be done here for ANON_USER_ID
        user_id_string = ""
        if param_name:
            user_id_string = ('&amp;{param_name}={anon_user_id}').format(
                param_name=param_name,
                anon_user_id=anon_user_id,
            )

        html_source = self.get_resource_string('view.html')
        html_source = html_source.format(
            self=self,
            display_name=display_name,
            survey_id=survey_id,
            your_university=your_university,
            link_text=link_text,
            user_id_string=user_id_string,
        )

        fragment = self.build_fragment(
            html_source=html_source,
        )

        return fragment

    def get_resource_string(self, path):
        """
        Retrieve string contents for the file path
        """
        path = os.path.join('public', path)
        resource_string = pkg_resources.resource_string(__name__, path)
        return resource_string.decode('utf8')

    def get_resource_url(self, path):
        """
        Retrieve a public URL for the file path
        """
        path = os.path.join('public', path)
        resource_url = self.runtime.local_resource_url(self, path)
        return resource_url

    def build_fragment(self,
        html_source=None,
        path_css=None,
        path_js=None,
        fragment_js=None,
    ):
        """
        Assemble the HTML, JS, and CSS for an XBlock fragment
        """

        fragment = Fragment(html_source)
        if path_css:
            css_url = self.get_resource_url(path_css)
            fragment.add_css_url(css_url)
        if path_js:
            js_url = self.get_resource_url(path_js)
            fragment.add_javascript_url(js_url)
        if fragment_js:
            fragment.initialize_js(fragment_js)

        return fragment
