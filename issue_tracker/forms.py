from django import forms
from .models import Comment,Issue

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class IssueForm(forms.ModelForm):
    def __int__(self, *args, disabled_project=True, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['project'].disabled = disabled_project
    class Meta:
        model = Issue
        fields = ('title','content','project', 'is_draft')


class NewIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title','content','project', 'is_draft')

