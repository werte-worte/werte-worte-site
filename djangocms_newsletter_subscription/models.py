# -*- coding: utf-8 -*-

from cms.models import CMSPlugin
from django.db import models
from newsletter.forms import SubscribeRequestForm
from newsletter.models import Newsletter


class NewsletterSubscription(CMSPlugin):
    """
    A Newsletter Subscription Form Plugin for 'newsletter'
    """

    target_newsletter = models.ForeignKey(Newsletter)
    form_title = models.TextField(blank=True)

    @property
    def subscription_form(self):
        return SubscribeRequestForm(newsletter=self.target_newsletter)

    def __str__(self):
        return str(self.target_newsletter)
