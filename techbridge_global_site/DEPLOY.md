# Deploy TechBridge Global Website

This guide covers deploying to **Render** (recommended — free tier, PostgreSQL included).

## Before you deploy

1. Push the project to **GitHub** (repo root can be `TechBridge_Global_Django_Website` or `techbridge_global_site`).
2. Set the **Root Directory** to `techbridge_global_site` if the repo contains the parent folder.

## Option A — Render Blueprint (easiest)

1. Go to [render.com](https://render.com) and sign up.
2. Click **New → Blueprint**.
3. Connect your GitHub repo.
4. Render reads `render.yaml` and creates:
   - A **PostgreSQL** database
   - A **Web Service** for Django
5. After deploy, open the web service **Environment** tab and set:
   - `ALLOWED_HOSTS` → your Render URL, e.g. `techbridge-global.onrender.com`
   - `CSRF_TRUSTED_ORIGINS` → `https://techbridge-global.onrender.com`
6. Optional — for **logo uploads** that persist across redeploys:
   - Create a free account at [cloudinary.com](https://cloudinary.com)
   - Add env var `CLOUDINARY_URL` → `cloudinary://API_KEY:API_SECRET@CLOUD_NAME`

### First-time setup on Render

Open the web service **Shell** and run:

```bash
python manage.py createsuperuser
python manage.py seed_site
```

Then sign in at `https://your-app.onrender.com/panel/`.

---

## Option B — Render manual setup

1. **New → PostgreSQL** (free) — copy the **Internal Database URL**.
2. **New → Web Service** → connect repo.
3. Settings:
   - **Root Directory:** `techbridge_global_site`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn techbridge_global.wsgi:application --bind 0.0.0.0:$PORT`
4. Environment variables:

| Variable | Value |
|----------|--------|
| `SECRET_KEY` | long random string |
| `DEBUG` | `False` |
| `DATABASE_URL` | PostgreSQL connection string from step 1 |
| `ALLOWED_HOSTS` | your-app.onrender.com |
| `CSRF_TRUSTED_ORIGINS` | https://your-app.onrender.com |
| `CLOUDINARY_URL` | optional, for logo/media |

5. Deploy, then run `createsuperuser` and `seed_site` in the Shell.

---

## Option C — Railway

1. Push to GitHub.
2. [railway.app](https://railway.app) → **New Project → Deploy from GitHub**.
3. Add a **PostgreSQL** plugin — Railway sets `DATABASE_URL` automatically.
4. Set root directory to `techbridge_global_site` if needed.
5. Variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`.
6. **Start command:** `gunicorn techbridge_global.wsgi:application --bind 0.0.0.0:$PORT`
7. **Build:** `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`

---

## Custom domain

After deploy works on the default URL:

1. Add your domain in the host platform (Render → Settings → Custom Domains).
2. Update DNS as instructed (usually a CNAME).
3. Set environment variables:
   - `ALLOWED_HOSTS` → `yourdomain.com,www.yourdomain.com`
   - `CSRF_TRUSTED_ORIGINS` → `https://yourdomain.com,https://www.yourdomain.com`

---

## Production checklist

- [ ] `DEBUG=False`
- [ ] Strong `SECRET_KEY` (not the dev default)
- [ ] PostgreSQL via `DATABASE_URL` (not SQLite)
- [ ] `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` set
- [ ] Admin password changed from default
- [ ] `CLOUDINARY_URL` set if using logo uploads
- [ ] `python manage.py seed_site` run once on production DB

---

## Local production test

```powershell
cd techbridge_global_site
.\.venv\Scripts\activate
pip install -r requirements.txt
$env:DEBUG="False"
python manage.py collectstatic --no-input
python manage.py check --deploy
gunicorn techbridge_global.wsgi:application --bind 127.0.0.1:8000
```
