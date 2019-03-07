"""
Test the Qualtrics Survey XBlock
"""
import unittest

import mock
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from xblock.field_data import DictFieldData

from qualtricssurvey.qualtricssurvey import QualtricsSurvey


def make_an_xblock(**kwargs):
    """
    Create and return an instance of the XBlock
    """
    course_id = SlashSeparatedCourseKey('foo', 'bar', 'baz')
    runtime = mock.Mock(course_id=course_id)
    scope_ids = mock.Mock()
    field_data = DictFieldData(kwargs)
    xblock = QualtricsSurvey(runtime, field_data, scope_ids)
    xblock.xmodule_runtime = runtime
    return xblock


class QualtricsSurveyXblockTests(unittest.TestCase):
    """
    Test the XBlock
    """

    def test_student_view(self):
        """
        Checks the student view with param_name but without
        anonymous_user_id.
        """
        xblock = make_an_xblock()
        fragment = xblock.student_view()
        url_frag = (
            'href="https://stanforduniversity.qualtrics.com/jfe/form/Enter '
            'your survey ID here.&quest;a='
        )
        self.assertIn(url_frag, fragment.content)
        url_frag = '>" target="_blank">Begin Survey'
        self.assertIn(url_frag, fragment.content)
        message_html = '<p>' + xblock.message + '</p>'
        self.assertIn(message_html, fragment.content)

    def test_student_view_no_param_name(self):
        """
        Checks the student view without param_name;
        user id part should be missing.
        """
        xblock = make_an_xblock(param_name=None)
        fragment = xblock.student_view()
        url = (
            '"https://stanforduniversity.qualtrics.com/'
            'jfe/form/Enter your survey ID '
            'here." target="_blank">Begin Survey'
        )
        self.assertIn(url, fragment.content)

    def test_custom_message(self):
        """
        Checks the student view with a custom message.
        """
        message = "test message"
        xblock = make_an_xblock()
        xblock.message = message
        fragment = xblock.student_view()
        message_html = '<p>' + message + '</p>'
        self.assertIn(message_html, fragment.content)
