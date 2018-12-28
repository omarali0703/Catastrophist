from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from catastrophist.stories.models import Story, StoryBlock

# Create your views here.
class StoriesView(ListView):
    template_name = "pages/stories.html"
    model = Story
    context_object_name = 'story_list'

    #def get_context_view(self, **kwargs):
    #    context = super(ListView, self).get_context_data(**kwargs)
    #    context['blocks'] = StoryBlock.objects.all()
    #    return context

class StoriesToBlockView(ListView):
    template_name = "pages/stories.html"
    context_object_name = 'block_list'

    def get_context_data(ListView, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story_list'] = Story.objects.all()
        return context

    def get_queryset(self):
        q = StoryBlock.objects.all()
        return q

class UserStoriesView(ListView):
    template_name = "users/user_detail.html"
    model = Story
    context_object_name = 'story_list'
