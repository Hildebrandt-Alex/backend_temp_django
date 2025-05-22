# create_superuser.py
import os
import django
from decouple import config
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_temp.settings")
django.setup()

User = get_user_model()

if not User.objects.filter(username=config('DJANGO_SUPERUSER_USERNAME')).exists():
    User.objects.create_superuser(
        username=config('DJANGO_SUPERUSER_USERNAME'),
        email=config('DJANGO_SUPERUSER_EMAIL'),
        password=config('DJANGO_SUPERUSER_PASSWORD')
    )
    print("✅ Superuser wurde erstellt.")
else:
    print("ℹ️ Superuser existiert bereits.")
