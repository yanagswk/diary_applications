from django import forms
from django.core.mail import EmailMessage
from django.forms import ModelForm, TextInput, Textarea

from .models import Journal, Comment, Reply





class JournalCreateForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ('title', 'category', 'tags', 'content', 'picture1', 'picture2', 'picture3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'





class JournalCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'コメント',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }


class JournalReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'content')
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '返信',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }