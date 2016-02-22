# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from djangocms_style.models import Style

from .models import NewsletterSubscription

class NewsletterSubscriptionPlugin(CMSPluginBase):
    model = NewsletterSubscription
    name = "Newletter Subscription Form"
    render_template = "cms/plugins/newsletter_subscription.html"


plugin_pool.register_plugin(NewsletterSubscriptionPlugin)
