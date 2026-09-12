"""
Django Blog API using Django REST Framework.
Implements CRUD operations for a Post model.
"""

# backend/day2/django_blog/blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]