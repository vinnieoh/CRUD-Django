from django.db import models


class Produto(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name ='produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.produto

