from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, TemplateView
from catastrophist.stories.models import Story, StoryBlock
from .forms import AddBlockForm
from django.http import HttpResponseRedirect
# Create your views here.
class StoriesView(ListView):
    template_name = "pages/stories.html"
    model = Story
    context_object_name = 'story_list'

class UserStoriesView(ListView):
    template_name = "users/user_detail.html"
    model = Story
    context_object_name = 'story_list'

class AddBlockView(UpdateView):
    model = StoryBlock
    def get_object(self):
        return StoryBlock.objects.get(id=1)

    title = StoryBlock.objects.get(id=1).story.story_name

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    fields=["body_text"]
