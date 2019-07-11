"""
This is the core logic for the XBlock
"""
from __future__ import absolute_import
from xblock.core import XBlock

from .mixins.scenario import XBlockWorkbenchMixin
from .models import QualtricsSurveyModelMixin
from .views import QualtricsSurveyViewMixin


@XBlock.needs('i18n')
class QualtricsSurvey(
        QualtricsSurveyModelMixin,
        QualtricsSurveyViewMixin,
        XBlockWorkbenchMixin,
        XBlock,
):
    """
    A Qualtrics survey XBlock.
    """
