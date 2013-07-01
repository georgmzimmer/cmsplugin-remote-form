from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.conf import settings



class ContactForm(forms.Form):
    email 	= forms.EmailField() 
    phone 	= forms.CharField()
    subject	= forms.CharField()
    content	= forms.CharField(widget=forms.Textarea())

    def send(self, site_email):
        current_site = Site.objects.get_current()
        
        email_message = EmailMessage(
            # self.cleaned_data['subject'],
            "[" + current_site.domain.upper() + "]",
                render_to_string("email.txt", {
                    'data': self.cleaned_data,
            }),
                    from_email = None,  #site_email, => settings.DEFAULT_FROM_EMAIL
                    to = site_email.split(','),
                    headers = {
                'Reply-To': self.cleaned_data['email']
                },)
        email_message.send(fail_silently=True)
