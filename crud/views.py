from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto


class HomeView(ListView):
    produto = Produto
    template_name = 'home.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
