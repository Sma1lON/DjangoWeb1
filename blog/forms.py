from django.forms import ModelForm
from .models import Comments, Blog


class NewPost(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text','text_min', 'tags', 'description', 'keywords', 'category' )


class ArticleForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ('user',)


class CommentForms(ModelForm):
    """Форма коментарів"""

    class Meta:
        model = Comments
        fields = ('text',)
