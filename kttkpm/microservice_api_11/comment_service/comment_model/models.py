from django.db import models

# Create your models here.

class Comment(models.Model):
    id_user = models.CharField(max_length=255)
    id_product = models.CharField(max_length=255)
    category_product = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id_user} {self.id_product} {self.category_product} {self.content} {self.date}'
