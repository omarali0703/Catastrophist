from django import forms
from  .models import StoryBlock

class AddBlock(forms.Form):
    body_text = forms.CharField(widget=forms.TextInput)

    def post(self):
        print("NEW BLOCK")

    class Meta:
        model = StoryBlock
        fields=('body_text', )
