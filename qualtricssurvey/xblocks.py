"""
This is the core logic for the XBlock
"""

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
