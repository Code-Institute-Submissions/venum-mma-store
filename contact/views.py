from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact
import os


ADMINS_EMAIL = os.environ.get('ADMINS_EMAIL')


def contactView(request):

    if request.method == 'POST':
        if request.user.is_authenticated:

            form = Contact(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                subject=request.POST['subject'],
                from_email=request.POST['from_email'],
                message=request.POST['message'],
            )

            form.save()

        else:
            form = Contact(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                subject=request.POST['subject'],
                from_email=request.POST['from_email'],
                message=request.POST['message'],
            )

            form.save()

        send_mail(
            'User contacted you.',
            'See message in panel.',
            os.environ.get('SITE_EMAIL'),
            [ADMINS_EMAIL],
            fail_silently=False,
        )

        return redirect('success')

    else:
        if request.user.is_authenticated:
            form = ContactForm()

    context = {
        'contact_page': 'active',
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def successView(request):
    return render(request, 'contact/success.html')
