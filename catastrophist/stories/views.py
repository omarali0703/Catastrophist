from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from catastrophist.stories.models import Story

# Create your views here.
class StoriesView(ListView):
    template_name = "pages/stories.html"
    model = Story
    context_object_name = 'story_list'
