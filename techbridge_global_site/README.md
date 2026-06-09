# TechBridge Global Limited - Django Website

Professional Django starter website for IT/software development, high-tech recruitment, relocation and business support services.

## Features

- Custom dynamic admin panel at `/panel/`
- Dynamic company settings managed from the panel
- Upload and manage company logo
- Dynamic service categories and service items
- Dynamic process steps, FAQs and testimonials
- Contact enquiry form stored in admin panel
- High-tech responsive design
- Ready for Cursor / VS Code development

## Quick Start

```powershell
cd techbridge_global_site
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py shell < seed_data.py
python manage.py createsuperuser
python manage.py runserver
```

Open:

- Website: http://127.0.0.1:8000/
- Dynamic Admin Panel: http://127.0.0.1:8000/panel/
- Django Admin (advanced): http://127.0.0.1:8000/admin/

## What to manage in the dynamic panel

1. Company Settings: company name, logo, email, phone, address, hero text, buttons.
2. Service Categories: add/remove main service blocks.
3. Service Items: add detailed items under each service.
4. Process Steps: change workflow.
5. FAQ: update common questions.
6. Contact Messages: view enquiries from website visitors.

## Deploy to production

See **[DEPLOY.md](DEPLOY.md)** for step-by-step instructions (Render, Railway, custom domain).

Quick summary:

1. Push code to GitHub.
2. Deploy on Render using `render.yaml` (PostgreSQL + web service).
3. Set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` to your live URL.
4. Run `python manage.py createsuperuser` and `python manage.py seed_site` in the host shell.
5. Optional: add `CLOUDINARY_URL` for persistent logo uploads.
