from django.db import models


class Produto(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    def __str__(self):
        return self.produto

