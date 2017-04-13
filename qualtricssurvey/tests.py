import mock
import unittest

from opaque_keys.edx.locations import SlashSeparatedCourseKey
from xblock.field_data import DictFieldData

from qualtricssurvey import QualtricsSurvey


class QualtricsSurveyXblockTests(unittest.TestCase):

    def make_an_xblock(self, **kw):

        course_id = SlashSeparatedCourseKey('foo', 'bar', 'baz')
        runtime = mock.Mock(course_id=course_id)
        scope_ids = mock.Mock()

        field_data = DictFieldData(kw)
        xblock = QualtricsSurvey(runtime, field_data, scope_ids)
        xblock.xmodule_runtime = runtime
        return xblock

    def test_student_view(self):
        """
        Checks the student view with param_name but without
        anonymous_user_id.
        """

        xblock = self.make_an_xblock()
        fragment = xblock.student_view()

        url_frag = (
            'href="https://stanforduniversity.qualtrics.com/jfe/form/Enter '
            'your survey ID here.&quest;a='
        )
        self.assertIn(url_frag, fragment.content)
        url_frag = '>" target="_blank">Begin Survey'
        self.assertIn(url_frag, fragment.content)

    def test_student_view_no_param_name(self):
        """
        Checks the student view without param_name;
        user id part should be missing.
        """

        xblock = self.make_an_xblock(param_name=None)
        fragment = xblock.student_view()

        url = (
            '"https://stanforduniversity.qualtrics.com/jfe/form/Enter your survey ID '
            'here." target="_blank">Begin Survey'
        )
        self.assertIn(url, fragment.content)
