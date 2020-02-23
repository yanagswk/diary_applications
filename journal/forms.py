from django import forms
from django.core.mail import EmailMessage

from .models import Journal


class JournalCreateForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


