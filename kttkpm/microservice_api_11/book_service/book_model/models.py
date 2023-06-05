from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.author} {self.amount} {self.description} {self.price} {self.category}'