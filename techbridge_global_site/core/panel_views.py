from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    CompanySettings,
    ContactMessage,
    FAQ,
    ProcessStep,
    ServiceCategory,
    ServiceItem,
    Testimonial,
)
from .panel_decorators import staff_required
from .panel_forms import (
    CompanySettingsForm,
    ContactMessageStatusForm,
    FAQForm,
    PanelLoginForm,
    ProcessStepForm,
    ServiceCategoryForm,
    ServiceItemForm,
    TestimonialForm,
)


def panel_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('panel_dashboard')

    form = PanelLoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        messages.success(request, 'Welcome to the admin panel.')
        return redirect('panel_dashboard')

    return render(request, 'panel/login.html', {'form': form})


def panel_logout(request):
    logout(request)
    messages.info(request, 'You have been signed out.')
    return redirect('panel_login')


@staff_required
def panel_dashboard(request):
    return render(request, 'panel/dashboard.html', {
        'stats': {
            'services': ServiceCategory.objects.count(),
            'service_items': ServiceItem.objects.count(),
            'process_steps': ProcessStep.objects.count(),
            'testimonials': Testimonial.objects.count(),
            'faqs': FAQ.objects.count(),
            'messages_total': ContactMessage.objects.count(),
            'messages_new': ContactMessage.objects.filter(is_processed=False).count(),
        },
        'recent_messages': ContactMessage.objects.all()[:5],
    })


@staff_required
def panel_settings(request):
    settings_obj, _ = CompanySettings.objects.get_or_create(
        company_name='TechBridge Global Limited',
    )
    form = CompanySettingsForm(request.POST or None, request.FILES or None, instance=settings_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Company settings updated.')
        return redirect('panel_settings')

    return render(request, 'panel/settings.html', {'form': form})


@staff_required
def panel_service_list(request):
    categories = ServiceCategory.objects.prefetch_related('items')
    return render(request, 'panel/service_list.html', {'categories': categories})


@staff_required
def panel_service_create(request):
    form = ServiceCategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        category = form.save()
        messages.success(request, f'Service category "{category.title}" created.')
        return redirect('panel_service_list')

    return render(request, 'panel/service_form.html', {
        'form': form,
        'title': 'Add Service Category',
    })


@staff_required
def panel_service_edit(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    form = ServiceCategoryForm(request.POST or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Service category updated.')
        return redirect('panel_service_list')

    return render(request, 'panel/service_form.html', {
        'form': form,
        'title': 'Edit Service Category',
        'category': category,
    })


@staff_required
def panel_service_delete(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    if request.method == 'POST':
        title = category.title
        category.delete()
        messages.success(request, f'Service category "{title}" deleted.')
        return redirect('panel_service_list')

    return render(request, 'panel/confirm_delete.html', {
        'object': category,
        'object_label': category.title,
        'cancel_url': 'panel_service_list',
    })


@staff_required
def panel_service_items(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    items = category.items.all()

    if request.method == 'POST':
        item_form = ServiceItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.category = category
            item.save()
            messages.success(request, f'Service item "{item.title}" added.')
            return redirect('panel_service_items', pk=pk)
    else:
        item_form = ServiceItemForm()

    return render(request, 'panel/service_items.html', {
        'category': category,
        'items': items,
        'item_form': item_form,
    })


@staff_required
def panel_service_item_edit(request, pk, item_pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    item = get_object_or_404(ServiceItem, pk=item_pk, category=category)
    form = ServiceItemForm(request.POST or None, instance=item)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Service item updated.')
        return redirect('panel_service_items', pk=pk)

    return render(request, 'panel/service_item_form.html', {
        'form': form,
        'category': category,
        'item': item,
    })


@staff_required
def panel_service_item_delete(request, pk, item_pk):
    category = get_object_or_404(ServiceCategory, pk=pk)
    item = get_object_or_404(ServiceItem, pk=item_pk, category=category)
    if request.method == 'POST':
        title = item.title
        item.delete()
        messages.success(request, f'Service item "{title}" deleted.')
        return redirect('panel_service_items', pk=pk)

    return render(request, 'panel/confirm_delete.html', {
        'object': item,
        'object_label': item.title,
        'cancel_url': 'panel_service_items',
        'cancel_url_kwargs': {'pk': pk},
    })


@staff_required
def panel_process_list(request):
    steps = ProcessStep.objects.all()
    return render(request, 'panel/process_list.html', {'steps': steps})


@staff_required
def panel_process_create(request):
    form = ProcessStepForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        step = form.save()
        messages.success(request, f'Process step "{step.title}" created.')
        return redirect('panel_process_list')

    return render(request, 'panel/process_form.html', {
        'form': form,
        'title': 'Add Process Step',
    })


@staff_required
def panel_process_edit(request, pk):
    step = get_object_or_404(ProcessStep, pk=pk)
    form = ProcessStepForm(request.POST or None, instance=step)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Process step updated.')
        return redirect('panel_process_list')

    return render(request, 'panel/process_form.html', {
        'form': form,
        'title': 'Edit Process Step',
        'step': step,
    })


@staff_required
def panel_process_delete(request, pk):
    step = get_object_or_404(ProcessStep, pk=pk)
    if request.method == 'POST':
        title = step.title
        step.delete()
        messages.success(request, f'Process step "{title}" deleted.')
        return redirect('panel_process_list')

    return render(request, 'panel/confirm_delete.html', {
        'object': step,
        'object_label': step.title,
        'cancel_url': 'panel_process_list',
    })


@staff_required
def panel_testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'panel/testimonial_list.html', {'testimonials': testimonials})


@staff_required
def panel_testimonial_create(request):
    form = TestimonialForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        testimonial = form.save()
        messages.success(request, f'Testimonial from "{testimonial.client_name}" created.')
        return redirect('panel_testimonial_list')

    return render(request, 'panel/testimonial_form.html', {
        'form': form,
        'title': 'Add Testimonial',
    })


@staff_required
def panel_testimonial_edit(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    form = TestimonialForm(request.POST or None, instance=testimonial)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Testimonial updated.')
        return redirect('panel_testimonial_list')

    return render(request, 'panel/testimonial_form.html', {
        'form': form,
        'title': 'Edit Testimonial',
        'testimonial': testimonial,
    })


@staff_required
def panel_testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        name = testimonial.client_name
        testimonial.delete()
        messages.success(request, f'Testimonial from "{name}" deleted.')
        return redirect('panel_testimonial_list')

    return render(request, 'panel/confirm_delete.html', {
        'object': testimonial,
        'object_label': testimonial.client_name,
        'cancel_url': 'panel_testimonial_list',
    })


@staff_required
def panel_faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'panel/faq_list.html', {'faqs': faqs})


@staff_required
def panel_faq_create(request):
    form = FAQForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        faq = form.save()
        messages.success(request, 'FAQ created.')
        return redirect('panel_faq_list')

    return render(request, 'panel/faq_form.html', {
        'form': form,
        'title': 'Add FAQ',
    })


@staff_required
def panel_faq_edit(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    form = FAQForm(request.POST or None, instance=faq)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'FAQ updated.')
        return redirect('panel_faq_list')

    return render(request, 'panel/faq_form.html', {
        'form': form,
        'title': 'Edit FAQ',
        'faq': faq,
    })


@staff_required
def panel_faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == 'POST':
        question = faq.question
        faq.delete()
        messages.success(request, f'FAQ "{question}" deleted.')
        return redirect('panel_faq_list')

    return render(request, 'panel/confirm_delete.html', {
        'object': faq,
        'object_label': faq.question,
        'cancel_url': 'panel_faq_list',
    })


@staff_required
def panel_message_list(request):
    message_list = ContactMessage.objects.all()
    return render(request, 'panel/message_list.html', {'message_list': message_list})


@staff_required
def panel_message_detail(request, pk):
    message_obj = get_object_or_404(ContactMessage, pk=pk)
    form = ContactMessageStatusForm(request.POST or None, instance=message_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Message status updated.')
        return redirect('panel_message_detail', pk=pk)

    return render(request, 'panel/message_detail.html', {
        'message_obj': message_obj,
        'form': form,
    })
