from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        # since form fields werent directly mentioned we have to use it like this 
        # check https://docs.djangoproject.com/en/4.0/ref/forms/widgets/ for more info
        # overriding default form setting and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs = {'placeholder': 'Enter name', }
        self.fields['body'].widget.attrs = {'placeholder': 'Comment here...','rows':'5','id':'textArea'}