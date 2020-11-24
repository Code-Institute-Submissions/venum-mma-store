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
                  'from_email',
                  'subject',
                  'message']

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
