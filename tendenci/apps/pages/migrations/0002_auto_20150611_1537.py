# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import tendenci.apps.user_groups.utils


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_groups', '0001_initial'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='group',
            field=models.ForeignKey(default=tendenci.apps.user_groups.utils.get_default_group, to='user_groups.Group', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='header_image',
            field=models.ForeignKey(to='pages.HeaderImage', null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta',
            field=models.OneToOneField(null=True, to='meta.Meta'),
        ),
        migrations.AddField(
            model_name='page',
            name='owner',
            field=models.ForeignKey(related_name='pages_page_owner', on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
