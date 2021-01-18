"""
Handle data access logic for the XBlock
"""

from django.utils.translation import ugettext_lazy as _
from xblock.fields import Scope
from xblock.fields import String


class QualtricsSurveyModelMixin:
    """
    Handle data access for XBlock instances
    """

    editable_fields = [
        'display_name',
        'survey_id',
        'your_university',
        'link_text',
        'param_name',
        'message',
    ]
    display_name = String(
        display_name=_('Display Name:'),
        default='Qualtrics Survey',
        scope=Scope.settings,
        help=_(
            'This name appears in the horizontal navigation at the top '
            'of the page.'
        ),
    )
    link_text = String(
        display_name=_('Link Text:'),
        default='Begin Survey',
        scope=Scope.settings,
        help=_('This is the text that will link to your survey.'),
    )
    message = String(
        display_name=_('Message:'),
        default='The survey will open in a new browser tab or window.',
        scope=Scope.settings,
        help=_(
            'This is the text that will be displayed '
            'above the link to your survey.'
        ),
    )
    param_name = String(
        display_name=_('Param Name:'),
        default='a',
        scope=Scope.settings,
        help=_(
            'This is the name for the User ID parameter in the url. '
            'If blank, User ID is ommitted from the url.'
        ),
    )
    survey_id = String(
        display_name=_('Survey ID:'),
        default='Enter your survey ID here.',
        scope=Scope.settings,
        help=_(
            'This is the ID that Qualtrics uses for the survey, which can '
            'include numbers and letters, and should be entered in the '
            'following format: SV_###############'
        ),
    )
    your_university = String(
        display_name=_('Your University:'),
        default='stanforduniversity',
        scope=Scope.settings,
        help=_('This is the name of your university.'),
    )

    # pylint: disable=no-member
    def get_anon_id(self):
        """
        Return an anonymous user id
        """
        try:
            user_id = self.xmodule_runtime.anonymous_student_id
        except AttributeError:
            user_id = -1
        return user_id
    # pylint: enable=no-member
