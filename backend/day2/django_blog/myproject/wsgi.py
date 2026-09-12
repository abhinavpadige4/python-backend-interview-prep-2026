"""
Django Blog API using Django REST Framework.
Implements CRUD operations for a Post model.
"""

# backend/day2/django_blog/myproject/wsgi.py
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()