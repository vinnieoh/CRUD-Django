from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class AdminProduto(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'preco')

