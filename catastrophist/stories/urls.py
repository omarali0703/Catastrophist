from django.urls import path

from catastrophist.stories.views import StoriesView, StoriesToBlockView

app_name = "stories"
urlpatterns = [
#    path("stories/", view=StoriesView.as_view(), name="stories"),
    path("stories/", view=StoriesToBlockView.as_view(), name="stories"),

]
