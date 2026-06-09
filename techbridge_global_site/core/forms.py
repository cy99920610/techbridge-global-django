from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'company', 'email', 'phone', 'service_interest', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone / WhatsApp'}),
            'service_interest': forms.TextInput(attrs={'placeholder': 'Software, recruitment, relocation, consulting...'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us what support you need', 'rows': 5}),
        }
