import re

from django import forms
from django.forms import Textarea, TextInput

from app.models.questions import Question


def tags_list_valid(value):
    if not re.match(r'^\w*[,?\s?\w+]+$', value):
        raise forms.ValidationError("Тэги должны быть разделены ,")


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content', 'tags')
        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control-sm', 'placeholder': "Enter title"}),
            'content': Textarea(attrs={
                'class': 'form-control-sm', 'placeholder': "Enter text a question"}),
            'tags': TextInput(attrs={
                'class': 'form-control-sm', 'placeholder': "Enter tags with ,"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].validators = [tags_list_valid]
        self.fields['tags'].help_text = "Тэги должны быть разделены ,"
        # self.fields['username'].widget.attrs.update({
        #     'class': 'form-control-sm'})
