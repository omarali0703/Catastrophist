from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

app_name = "stories"
urlpatterns = [
    path("", view=StoriesView.as_view(), name="stories"),
    path("addblock/", view=AddBlockView.as_view(), name="addblock"),
    path("addstory/", view=login_required(AddStoryView.as_view()), name='addstory'),
]
