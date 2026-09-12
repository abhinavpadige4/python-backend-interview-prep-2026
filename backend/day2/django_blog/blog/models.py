"""
Django Blog API using Django REST Framework.
Implements CRUD operations for a Post model.
"""

# backend/day2/django_blog/blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title