from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.state}"


class ProtectedArea(models.Model):
    CATEGORY_CHOICES = [
        ('NP', 'National Park'),
        ('WS', 'Wildlife Sanctuary')
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    established_year = models.PositiveIntegerField(null=True, blank=True)
    area_sq_km = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    official_website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"