from django.conf.urls import *  # NOQA

from djangocms_newsletter_subscription.views import EmbeddedFormSubscribeRequestView

urlpatterns = patterns('',
    url(r'subscribe/(?P<newsletter_slug>\S+)/',
        EmbeddedFormSubscribeRequestView.as_view(),
        name='newsletter_embedded_subscribe'
        )
)
