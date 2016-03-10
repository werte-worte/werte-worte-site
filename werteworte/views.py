from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from .forms import WriteMeAnEmailForm


def write_me(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WriteMeAnEmailForm(request.POST)
        if form.is_valid():
            subject = "Mail vom Formular: " + (form.cleaned_data['subject'] or "[kein Betreff]")
            sender = form.cleaned_data['email'] or "anonym@werteworte.org"
            send_mail(subject, form.cleaned_data['mailtext'], sender,
                      ['jo@werteworte.org'], fail_silently=False)
            messages.info(request, "Deine Nachricht wurde verschicht. Vielen Dank für deine Gedanken!")
            return redirect(reverse('pages-root'))
        else:
            flattended_messages = (e for el in form.errors.values() for e in el)
            messages.error(request, "Leider konnten wir deine Nachricht nicht verschicken:" +
                            ", ".join(flattended_messages))

            return redirect(reverse('pages-root'))
    else:
        form = WriteMeAnEmailForm()
        return render(request, 'write_me_popup', {'email_form': form})
