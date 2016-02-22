# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('newsletter', '0002_auto_20150416_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', auto_created=True, primary_key=True, serialize=False, parent_link=True)),
                ('form_title', models.TextField(blank=True)),
                ('target_newsletter', models.ForeignKey(to='newsletter.Newsletter')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
