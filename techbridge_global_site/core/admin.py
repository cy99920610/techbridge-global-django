from django.contrib import admin
from .models import CompanySettings, ServiceCategory, ServiceItem, ProcessStep, Testimonial, FAQ, ContactMessage

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1

@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Details', {'fields': ('company_name', 'tagline', 'logo', 'email', 'phone', 'address', 'linkedin', 'website')}),
        ('Homepage Hero', {'fields': ('hero_title', 'hero_subtitle', 'primary_button_text', 'secondary_button_text')}),
        ('Footer', {'fields': ('footer_note',)}),
    )

    def has_add_permission(self, request):
        return not CompanySettings.objects.exists()

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')
    inlines = [ServiceItemInline]

@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'is_active')
    list_display_links = ('title',)
    list_editable = ('number', 'is_active')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_role', 'is_active')
    list_editable = ('is_active',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'service_interest', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'company', 'email', 'message')
    readonly_fields = ('created_at',)
