from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(" ", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tags = models.CharField(max_length=100, default=" ", blank=True)

    def __str__(self):
        return f"Name: {self.name}"

class Coaches(models.Model):
    First = models.CharField(max_length=20)
    Last = models.CharField(max_length=50, default=" ")
    Age = models.IntegerField(default=0)
    Email = models.EmailField(max_length=200, default=" ", blank=True)

    def __str__(self):
        return f"FirstName: {self.First}, LastName: {self.Last}, Age: {self.Age}"
