from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, TemplateView, FormView
from django.forms import ModelForm
from django.http import HttpResponseRedirect

from .forms import AddStoryForm, AddBlockForm
from .models import Story, StoryBlock


# Create your views here.
class StoriesView(ListView):
    template_name = "pages/stories.html"
    model = Story
    context_object_name = 'story_list'

    def block_list(self):
        return StoryBlock.objects.all()


class UserStoriesView(ListView):
    template_name = "users/user_detail.html"
    model = Story
    context_object_name = 'story_list'
    test = "ss"

    def block_list(self):
        return StoryBlock.objects.all()


class AddBlockView(UpdateView):
    fields = ["body_text", "story"]
    model = StoryBlock

    def get_object(self):
        return StoryBlock.objects.all().first()

#    def form_valid(self, form):
#        StoryBlock.objects.create( **form.cleaned_data)
#        return super().form_valid(form)

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class AddStoryView(FormView):
    form_class = AddStoryForm
    template_name = 'stories/story_form.html'

    def form_valid(self, form):
        Story.objects.create(user_creator_id=self.request.user.id, **form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})
