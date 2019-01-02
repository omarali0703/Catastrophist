from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, DetailView, ListView, RedirectView, UpdateView, CreateView, TemplateView, FormView
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

class AddStoryView(FormView):
    form_class = AddStoryForm
    template_name = 'stories/story_form.html'

    def form_valid(self, form):
        Story.objects.create(user_creator_id=self.request.user.id, **form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

class AddBlockView(FormView):
    form_class = AddBlockForm
    template_name = 'stories/storyblock_form.html'
    id = 0
    title = ""
    s = ""
    def get_context_data(self, **kwargs):

        self.id = int(self.request.GET.get('id', -1))
        self.s = Story.objects.get(id=self.request.GET.get('id'));
        self.title = Story.objects.get(id=self.request.GET.get('id')).story_name
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        StoryBlock.objects.create(story=Story.objects.get(id=self.request.GET.get('id')), **form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

class RemoveBlockView(View):
    model = StoryBlock
    title = ""

    def get(self, request, *args, **kwargs):
        blockid = self.request.GET.get('blockid', -1)
        StoryBlock.objects.filter(id=blockid).delete()
        return HttpResponseRedirect(reverse("users:detail", args={self.request.user.username}))

class RemoveStoryView(View):
    model = Story
    title = ""

    def get(self, request, *args, **kwargs):
        story = self.request.GET.get('id', -1)
        Story.objects.filter(id=story).delete()
        return HttpResponseRedirect(reverse("users:detail", args={self.request.user.username}))
