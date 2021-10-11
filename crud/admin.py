from django.contrib import admin
from django.db import models

from .models import Produto


@admin.register(Produto)
class AdminProduto(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'preco')

