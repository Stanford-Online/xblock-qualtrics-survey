"""
Handle view logic for the XBlock
"""
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin


class QualtricsSurveyViewMixin(
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
):
    """
    Handle view logic for the XBlock
    """

    loader = ResourceLoader(__name__)
    show_in_read_only_mode = True

    def provide_context(self, context=None):
        """
        Build a context dictionary to render the student view
        """
        context = context or {}
        context = dict(context)
        param_name = self.param_name
        anon_user_id = self.get_anon_id()
        user_id_string = ''
        if param_name:
            user_id_string = f"?{param_name}={anon_user_id}"
        context.update({
            'xblock_id': str(self.scope_ids.usage_id),
            'survey_id': self.survey_id,
            'your_university': self.your_university,
            'link_text': self.link_text,
            'user_id_string': user_id_string,
            'message': self.message,
        })
        return context
