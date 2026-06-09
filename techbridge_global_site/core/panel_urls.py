from django.urls import path

from . import panel_views

urlpatterns = [
    path('login/', panel_views.panel_login, name='panel_login'),
    path('logout/', panel_views.panel_logout, name='panel_logout'),
    path('', panel_views.panel_dashboard, name='panel_dashboard'),
    path('settings/', panel_views.panel_settings, name='panel_settings'),
    path('services/', panel_views.panel_service_list, name='panel_service_list'),
    path('services/add/', panel_views.panel_service_create, name='panel_service_create'),
    path('services/<int:pk>/edit/', panel_views.panel_service_edit, name='panel_service_edit'),
    path('services/<int:pk>/delete/', panel_views.panel_service_delete, name='panel_service_delete'),
    path('services/<int:pk>/items/', panel_views.panel_service_items, name='panel_service_items'),
    path('services/<int:pk>/items/<int:item_pk>/edit/', panel_views.panel_service_item_edit, name='panel_service_item_edit'),
    path('services/<int:pk>/items/<int:item_pk>/delete/', panel_views.panel_service_item_delete, name='panel_service_item_delete'),
    path('process/', panel_views.panel_process_list, name='panel_process_list'),
    path('process/add/', panel_views.panel_process_create, name='panel_process_create'),
    path('process/<int:pk>/edit/', panel_views.panel_process_edit, name='panel_process_edit'),
    path('process/<int:pk>/delete/', panel_views.panel_process_delete, name='panel_process_delete'),
    path('testimonials/', panel_views.panel_testimonial_list, name='panel_testimonial_list'),
    path('testimonials/add/', panel_views.panel_testimonial_create, name='panel_testimonial_create'),
    path('testimonials/<int:pk>/edit/', panel_views.panel_testimonial_edit, name='panel_testimonial_edit'),
    path('testimonials/<int:pk>/delete/', panel_views.panel_testimonial_delete, name='panel_testimonial_delete'),
    path('faqs/', panel_views.panel_faq_list, name='panel_faq_list'),
    path('faqs/add/', panel_views.panel_faq_create, name='panel_faq_create'),
    path('faqs/<int:pk>/edit/', panel_views.panel_faq_edit, name='panel_faq_edit'),
    path('faqs/<int:pk>/delete/', panel_views.panel_faq_delete, name='panel_faq_delete'),
    path('messages/', panel_views.panel_message_list, name='panel_message_list'),
    path('messages/<int:pk>/', panel_views.panel_message_detail, name='panel_message_detail'),
]
