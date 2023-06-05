from django.db import models

# Create your models here.

class Order(models.Model):
    name_user = models.CharField(max_length=255)
    address_user = models.CharField(max_length=255)
    mobile_user = models.CharField(max_length=255)
    id_product = models.CharField(max_length=255)
    category_product = models.CharField(max_length=255)
    name_product = models.CharField(max_length=255)
    amount_product = models.IntegerField()
    description_product = models.TextField()
    price_product = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name_user} {self.address_user} {self.mobile_user} {self.name_product} {self.category_product} {self.date}'