from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form to allow the user to contact the site owners
    """
    class Meta:
        model = Contact
        fields = ['first_name',
                  'last_name',
                  'contact_subject',
                  'email',
                  'contact_body']

    first_name = forms.CharField(
        required=True,
        label='First Name:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        required=True,
        label='Last Name:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )

    contact_subject = forms.CharField(
        required=True,
        label='Subject:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject'
        })
    )

    email = forms.EmailField(
        required=True,
        label='Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )

    contact_body = forms.CharField(
        required=True,
        label='Please enter your message:',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message'
        })
    )
