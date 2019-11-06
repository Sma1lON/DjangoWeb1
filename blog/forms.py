from django.forms import ModelForm
from .models import Comments


class CommentForms(ModelForm):
    """Форма коментарів"""

    class Meta:
        model = Comments
        fields = ('text',)
