from django.core.mail import send_mail
from django.shortcuts import render, redirect
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
                from_email=request.POST['from_email'],
                subject=request.POST['subject'],
                message=request.POST['message'],
                query_user=request.user
            )

            form.save()

        else:
            form = ContactForm(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                from_email=request.POST['from_email'],
                subject=request.POST['subject'],
                message=request.POST['message'],
            )

            form.save()

            send_mail(
                'User has contacted our store',
                'Check admin panel.',
                os.environ.get('SITE_EMAIL'),
                [ADMINS_EMAIL],
                fail_silently=False,
            )
            return redirect('success')

    return render(request, 'contact/contact.html')


def successView(request):
    return render(request, 'contact/success.html')
