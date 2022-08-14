from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(" ", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tags = models.CharField(max_length=100, default=" ", blank=True)

    def __str__(self):
        return f"Name: {self.name}"
