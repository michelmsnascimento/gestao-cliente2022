from django.db import models


# Create your models here.
class Produto(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    photo = models.ImageField(upload_to='produtos_photos', null=True, blank=True)
    
    def __str__(self):
        return self.descricao
