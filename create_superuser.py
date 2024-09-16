import os
import django
from django.conf import settings
from django.contrib.auth import get_user_model

# Ensure Django is setup correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Replace 'your_project_name' with your actual Django project name
django.setup()

User = get_user_model()

# Only create the superuser if it doesn't exist
if not User.objects.filter(username=os.environ['DJANGO_SUPERUSER_USERNAME']).exists():
    User.objects.create_superuser(
        username=os.environ['DJANGO_SUPERUSER_USERNAME'],
        email=os.environ['DJANGO_SUPERUSER_EMAIL'],
        password=os.environ['DJANGO_SUPERUSER_PASSWORD']
    )
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")

