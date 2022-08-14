from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(" ")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=100, default=" ")

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"