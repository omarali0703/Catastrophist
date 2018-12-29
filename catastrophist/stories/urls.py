from django.urls import path

from catastrophist.stories.views import *
from catastrophist.users.views import user_update_view

app_name = "stories"
urlpatterns = [
    path("stories/", view=StoriesView.as_view(), name="stories"),
    path("addblock/", view=AddBlockView.as_view(), name="addblock"),


]
