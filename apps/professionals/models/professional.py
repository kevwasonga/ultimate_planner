from django.db import models
from .category import Category

class Professional(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('busy', 'Currently Busy'),
        ('unavailable', 'Unavailable'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='professionals')
    specialty = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    bio = models.TextField()
    experience_years = models.PositiveIntegerField(default=1)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField(blank=True)
    photo = models.ImageField(upload_to='professionals/', blank=True, null=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    projects_completed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', '-is_verified', 'name']

    def __str__(self):
        return f"{self.name} — {self.category.name}"

    @property
    def initials(self):
        parts = self.name.split()
        return ''.join(p[0] for p in parts[:2]).upper()

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return 0.0

    @property
    def review_count(self):
        return self.reviews.count()

    @property
    def price_display(self):
        return f"KSh {int(self.price_per_hour):,}/hr"
