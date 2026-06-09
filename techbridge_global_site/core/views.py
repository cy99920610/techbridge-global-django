from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .models import ServiceCategory, ProcessStep, Testimonial, FAQ


def home(request):
    categories = ServiceCategory.objects.filter(is_active=True).prefetch_related('items')[:6]
    steps = ProcessStep.objects.filter(is_active=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    faqs = FAQ.objects.filter(is_active=True)[:6]
    form = ContactMessageForm()
    return render(request, 'core/home.html', {
        'categories': categories,
        'steps': steps,
        'testimonials': testimonials,
        'faqs': faqs,
        'form': form,
    })


def services(request):
    categories = ServiceCategory.objects.filter(is_active=True).prefetch_related('items')
    return render(request, 'core/services.html', {'categories': categories})


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. Your enquiry has been received.')
            return redirect('contact')
    else:
        form = ContactMessageForm()
    return render(request, 'core/contact.html', {'form': form})
