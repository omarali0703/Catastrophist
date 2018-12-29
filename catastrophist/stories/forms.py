from django import forms
from  .models import StoryBlock

class AddBlockForm(forms.Form):
    text = forms.CharField(label="new block")
