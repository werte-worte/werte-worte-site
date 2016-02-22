from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from newsletter.views import SubscribeRequestView

# We adjust the request view from the newsletter app here to redirect to the current page
# with a success message when the successfully subscribed using out plugin
class EmbeddedFormSubscribeRequestView(SubscribeRequestView):
    def no_email_confirm(self, form):

        #TODO: check method to block multiple subscription with the same mail address
        # self._email_already_listed()

        self.subscription.update(self.action)

        messages.info(self.request, "Du wurdest in den Newsletter eingetragen. Vielen Dank für dein Interesse!")

        #TODO: conditionally use referrer header to stay on the same sub-page
        # (check whether referer path is valid page path!)
        return redirect(reverse('pages-root'))

    def form_invalid(self, form):
        flattended_messages = (e for el in form.errors.values() for e in el)
        messages.warning(self.request, "Wir konnten dich leider nicht in den Newsletter eintragen: " +
                         ", ".join(flattended_messages))

        #TODO: conditionally use referrer header to stay on the same sub-page
        # (check whether referer path is valid page path!)
        return redirect(reverse('pages-root'))
