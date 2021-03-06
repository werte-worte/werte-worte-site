# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import write_me

import os

CONFIGURATION = os.environ.get('DJANGO_CONFIGURATION', 'development').lower()

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^newsletter_subscription/', include('djangocms_newsletter_subscription.urls')),
    url(r'^cms_actions/write_me/?', write_me, name='write_me'),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA

if CONFIGURATION.startswith("dev"):
    import debug_toolbar
    urlpatterns = patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            ) + urlpatterns
