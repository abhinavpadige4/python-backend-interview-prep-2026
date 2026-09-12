"""
Django Blog API using Django REST Framework.
Implements CRUD operations for a Post model.
"""

# backend/day2/django_blog/myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]