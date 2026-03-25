from django.db import models
from django.db.models import Count, Sum
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=10, default='🏗️')
    description = models.TextField(blank=True)
    color = models.CharField(max_length=20, default='#C8860A')

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
