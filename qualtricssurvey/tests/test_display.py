#!/usr/bin/env python
"""
Test the Qualtrics Survey XBlock
"""
import unittest

from unittest import mock
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from xblock.field_data import DictFieldData

from qualtricssurvey.xblocks import QualtricsSurvey


def mock_an_xblock(**kwargs):
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


class TestRender(unittest.TestCase):
    """
    Test the HTML rendering of the XBlock
    """

    def setUp(self):
        self.xblock = mock_an_xblock()

    def test_render(self):
        student_view = self.xblock.student_view()
        html = student_view.content
        self.assertIsNotNone(html)
        self.assertNotEqual('', html)
        self.assertIn('qualtricssurvey_block', html)

    def test_student_view(self):
        """
        Checks the student view with param_name but without
        anonymous_user_id.
        """
        xblock = self.xblock
        fragment = xblock.student_view()
        content = fragment.content
        self.assertIn('Begin Survey', content)
        self.assertIn('target="_blank"', content)
        self.assertIn('a=', content)
        self.assertIn(
            'href="https://stanforduniversity.qualtrics.com/jfe/form/Enter',
            content
        )
        self.assertIn(xblock.message, content)

    def test_student_view_no_param_name(self):
        """
        Checks the student view without param_name;
        user id part should be missing.
        """
        xblock = mock_an_xblock(param_name=None)
        fragment = xblock.student_view()
        content = fragment.content
        self.assertNotIn('a=', content)

    def test_custom_message(self):
        """
        Checks the student view with a custom message.
        """
        message = 'test message'
        xblock = self.xblock
        xblock.message = message
        fragment = xblock.student_view()
        message_html = '<p>' + message + '</p>'
        content = fragment.content
        self.assertIn(message_html, content)


if __name__ == '__main__':
    unittest.main()
