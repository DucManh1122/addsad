from django.db import models

# Create your models here.

class Cart(models.Model):
    id_user = models.CharField(max_length=255)
    id_product = models.CharField(max_length=255)
    category_product = models.CharField(max_length=255)
    name_product = models.CharField(max_length=255)
    amount_product = models.IntegerField()
    description_product = models.TextField()
    price_product = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_user} {self.name_product} {self.category_product} {self.date}'