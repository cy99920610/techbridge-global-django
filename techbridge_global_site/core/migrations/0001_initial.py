# Generated manually for starter project
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='CompanySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='TechBridge Global Limited', max_length=160)),
                ('tagline', models.CharField(default='Technology, talent and relocation support for international companies.', max_length=220)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=80)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('linkedin', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('hero_title', models.CharField(default='Building the bridge between technology, talent and global mobility', max_length=220)),
                ('hero_subtitle', models.TextField(default='We provide software development, IT consulting, high-tech recruitment and relocation coordination for businesses growing across borders.')),
                ('primary_button_text', models.CharField(default='Explore Services', max_length=80)),
                ('secondary_button_text', models.CharField(default='Contact Us', max_length=80)),
                ('footer_note', models.CharField(default='International B2B technology and talent support services.', max_length=255)),
            ],
            options={'verbose_name': 'Company Settings', 'verbose_name_plural': 'Company Settings'},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('company', models.CharField(blank=True, max_length=160)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=80)),
                ('service_interest', models.CharField(blank=True, max_length=180)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=220)),
                ('answer', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['order', 'question']},
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['number']},
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('icon', models.CharField(default='✦', help_text='Use a short symbol or emoji, e.g. 💻, 👥, ✈️', max_length=40)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'verbose_name_plural': 'Service Categories', 'ordering': ['order', 'title']},
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=120)),
                ('client_role', models.CharField(blank=True, max_length=160)),
                ('quote', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.servicecategory')),
            ],
            options={'ordering': ['order', 'title']},
        ),
    ]
