from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.conf import settings

from .forms import WriteMeAnEmailForm

from urllib import parse as urlparse

class WriteMeAnEmailPlugin(CMSPluginBase):
    name = "Write Me an E-Mail Pop-Up"
    render_template = "cms/plugins/write_me_popup.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['email_form'] = WriteMeAnEmailForm
        return context

    def icon_src(self, instance):
        return urlparse.urljoin(
            settings.STATIC_URL, "cms/img/icons/plugins/snippet.png")


plugin_pool.register_plugin(WriteMeAnEmailPlugin)
