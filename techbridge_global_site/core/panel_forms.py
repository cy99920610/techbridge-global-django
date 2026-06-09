from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import (
    CompanySettings,
    ContactMessage,
    FAQ,
    ProcessStep,
    ServiceCategory,
    ServiceItem,
    Testimonial,
)


class PanelLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': True}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )


class CompanySettingsForm(forms.ModelForm):
    class Meta:
        model = CompanySettings
        fields = [
            'company_name', 'tagline', 'logo', 'email', 'phone', 'address',
            'linkedin', 'website', 'hero_title', 'hero_subtitle',
            'primary_button_text', 'secondary_button_text', 'footer_note',
        ]


class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['title', 'description', 'icon', 'order', 'is_active']


class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = ['title', 'description', 'order', 'is_active']


class ProcessStepForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = ['number', 'title', 'description', 'is_active']


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_role', 'quote', 'is_active']


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer', 'order', 'is_active']


class ContactMessageStatusForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['is_processed']
