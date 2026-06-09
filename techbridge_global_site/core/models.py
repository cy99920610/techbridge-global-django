from django.db import models

class CompanySettings(models.Model):
    company_name = models.CharField(max_length=160, default='TechBridge Global Limited')
    tagline = models.CharField(max_length=220, default='Technology, talent and relocation support for international companies.')
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=255, blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    hero_title = models.CharField(max_length=220, default='Building the bridge between technology, talent and global mobility')
    hero_subtitle = models.TextField(default='We provide software development, IT consulting, high-tech recruitment and relocation coordination for businesses growing across borders.')
    primary_button_text = models.CharField(max_length=80, default='Explore Services')
    secondary_button_text = models.CharField(max_length=80, default='Contact Us')
    footer_note = models.CharField(max_length=255, default='International B2B technology and talent support services.')

    class Meta:
        verbose_name = 'Company Settings'
        verbose_name_plural = 'Company Settings'

    def __str__(self):
        return self.company_name

class ServiceCategory(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    icon = models.CharField(max_length=40, default='✦', help_text='Use a short symbol or emoji, e.g. 💻, 👥, ✈️')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name_plural = 'Service Categories'

    def __str__(self):
        return self.title

class ServiceItem(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=160)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class ProcessStep(models.Model):
    number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}. {self.title}'

class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    client_role = models.CharField(max_length=160, blank=True)
    quote = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name

class FAQ(models.Model):
    question = models.CharField(max_length=220)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'question']

    def __str__(self):
        return self.question

class ContactMessage(models.Model):
    name = models.CharField(max_length=140)
    company = models.CharField(max_length=160, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=80, blank=True)
    service_interest = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.email}'
