from django.db import models
from django.db.models import Sum

class SiteStats(models.Model):
    cities_served = models.PositiveIntegerField(default=4)
    satisfaction_percent = models.PositiveIntegerField(default=98)
    tagline = models.CharField(max_length=200, default="Kenya's #1 Building Professionals Network")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    @classmethod
    def get_global_stats(cls):
        from .professional import Professional
        return {
            'settings': cls.get(),
            'total_professionals': Professional.objects.count(),
            'total_projects': Professional.objects.aggregate(total=Sum('projects_completed'))['total'] or 0,
        }
