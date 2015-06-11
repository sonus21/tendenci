# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rotator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_anonymous_view', models.BooleanField(default=True, verbose_name='Public can view')),
                ('allow_user_view', models.BooleanField(default=True, verbose_name='Signed in user can view')),
                ('allow_member_view', models.BooleanField(default=True)),
                ('allow_user_edit', models.BooleanField(default=False, verbose_name='Signed in user can change')),
                ('allow_member_edit', models.BooleanField(default=False)),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('creator_username', models.CharField(max_length=50)),
                ('owner_username', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name=b'Active')),
                ('status_detail', models.CharField(default=b'active', max_length=50)),
                ('position', models.IntegerField(default=0, null=True, verbose_name='Position', blank=True)),
                ('guid', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('content', models.TextField(blank=True)),
                ('syndicate', models.BooleanField(default=False, verbose_name='Include in RSS feed')),
                ('full_story_link', models.CharField(max_length=300, verbose_name='Full Story Link', blank=True)),
                ('link_title', models.CharField(max_length=200, verbose_name='Link Title', blank=True)),
                ('start_dt', models.DateTimeField(null=True, verbose_name='Start Date/Time', blank=True)),
                ('end_dt', models.DateTimeField(null=True, verbose_name='End Date/Time', blank=True)),
                ('expires', models.BooleanField(default=True, verbose_name='Expires')),
                ('tags', tagging.fields.TagField(default=b'', max_length=255, blank=True)),
                ('rotator_position', models.IntegerField(default=0, verbose_name='Rotator Position', blank=True)),
                ('creator', models.ForeignKey(related_name='stories_story_creator', on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('entity', models.ForeignKey(related_name='stories_story_entity', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='entities.Entity', null=True)),
            ],
            options={
                'ordering': ['position'],
                'verbose_name_plural': 'stories',
                'permissions': (('view_story', 'Can view story'),),
            },
        ),
        migrations.CreateModel(
            name='StoryPhoto',
            fields=[
                ('file_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='files.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('files.file',),
        ),
    ]
