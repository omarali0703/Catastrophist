from django import forms
from  .models import StoryBlock

class AddBlockForm(forms.Form):
    body_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}), label="body text")
