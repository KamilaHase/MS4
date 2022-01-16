from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """
    View to allow user to contact Good Oils admin
    """

    customer_email = request.POST.get('contact_email')

    if request.method == 'POST':
        contact_form = {
            'name': request.POST.get('name'),
            'email': request.POST.get('contact_email'),
            'contact_as': request.POST.get('contact_as'),
            'message': request.POST.get('message')
            }
        subject = render_to_string(
            'contact/contact_emails/contact_email_subject.txt',
            {'contact': contact_form}
        )
        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt',
            {'contact': contact_form}
        )
        send_mail(
            subject,
            body,
            customer_email,
            [settings.DEFAULT_FROM_EMAIL]
        )
        messages.success(request, 'Your message was sent successfully! Thank you.')

    else:
        messages.error(request, 'Sorry, there was an error with sending the message. Please try again')
    
    form = ContactForm

    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, 'contact/contact.html', context)