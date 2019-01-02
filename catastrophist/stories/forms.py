from django import forms

from  .models import *
from django.forms import ModelForm, Textarea

class AddBlockForm(forms.ModelForm):
    class Meta:
        model=StoryBlock
        fields = ["body_text"]

        widgets = {
            'body_text': Textarea(attrs={'cols': 80, 'rows': 10}),
        }
        #body_text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'class': 'textarea'}))

class AddStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields=['story_name', 'story_blurb']

        widgets = {
            'story_blurb': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

        #story_name = forms.CharField(widget=forms.Textarea(), label="story name")
        #story_blurb = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), label="story blurb")
