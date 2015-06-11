# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tendenci.apps.user_groups.utils
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_groups', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=tendenci.apps.user_groups.utils.get_default_group, to='user_groups.Group', null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='meta',
            field=models.OneToOneField(null=True, to='meta.Meta'),
        ),
        migrations.AddField(
            model_name='news',
            name='owner',
            field=models.ForeignKey(related_name='news_news_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='thumbnail',
            field=models.ForeignKey(default=None, to='news.NewsImage', help_text='The thumbnail image can be used on your homepage or sidebar if it is setup in your theme. The thumbnail image will not display on the news page.', null=True),
        ),
    ]
