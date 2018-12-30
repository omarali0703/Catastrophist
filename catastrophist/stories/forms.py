from django.forms import ModelForm, Form, CharField, Textarea
from  .models import StoryBlock, Story


class AddBlockForm(Form):
    body_text = CharField(widget=Textarea(attrs={'rows': 2, 'cols': 40}), label="body text")


class AddStoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['story_name', 'story_blurb']
