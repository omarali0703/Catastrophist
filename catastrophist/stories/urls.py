from django.urls import path

from catastrophist.stories.views import StoriesView

app_name = "stories"
urlpatterns = [
    path("stories/", view=StoriesView.as_view(), name="stories"),
]
