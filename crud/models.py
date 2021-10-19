from django.db import models


class Produto(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, blank=True)


    def __str__(self):
        return self.produto

