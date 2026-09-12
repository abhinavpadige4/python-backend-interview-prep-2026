"""
Django Blog API using Django REST Framework.
Implements CRUD operations for a Post model.
"""

# backend/day2/django_blog/myproject/asgi.py
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_asgi_application()