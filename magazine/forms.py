from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
""" Form for Post model """
    class Meta:
     """Create meta data to display Post form"""
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Sets autofocus on title, adds product form field
        """
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-product-form-field'


class CommentForm(forms.ModelForm):
""" Form for Comment model """
    class Meta:
        model = Comment
        fields = ['nickname', 'comment_text']

    def __init__(self, *args, **kwargs):
        """
        Sets label for comment field
        """
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_text'].label = "Comment"
