from django import forms

class WriteMeAnEmailForm(forms.Form):
    email = forms.EmailField(label = "Deine E-Mail Adresse (optional)", max_length=200, required=False)
    subject = forms.CharField(label= "Betreff", initial="WerteWorte", max_length=500)
    mailtext = forms.CharField(label="Dein Text", widget=forms.Textarea, required=True)
