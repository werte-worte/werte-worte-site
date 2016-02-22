from django import forms


class NewsletterSubscriptionForm(forms.Form):
    name = forms.CharField(label = "Dein Name (optional)", max_length=100)
    email = forms.EmailField(label = "E-Mail Adresse" , max_length=100)

