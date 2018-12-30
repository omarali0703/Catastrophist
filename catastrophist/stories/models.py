from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from catastrophist.users.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Story(models.Model): #built up of blocks by user, has a main author perhaps more authors later?
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    story_name = models.CharField(max_length=100, default='')
    story_blurb = models.CharField(max_length=1000, default='')


class StoryBlock(models.Model): #attached to a user, has text for just a block
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default='')
    body_text = models.CharField(max_length=1000, default='')
