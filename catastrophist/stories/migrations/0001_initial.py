# Generated by Django 2.1.4 on 2018-12-29 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_name', models.CharField(default='', max_length=100)),
                ('story_blurb', models.CharField(default='', max_length=1000)),
                ('user_creator', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoryBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.CharField(default='', max_length=1000)),
                ('story', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='stories.Story')),
            ],
        ),
    ]
