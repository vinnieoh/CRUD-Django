from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto


class HomeView(ListView):
    produto = Produto
    template_name = 'home.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    prduto = Produto
    template_name = 'prod_create_form.html'
    fields = ['produto', 'quantidade', 'preco']
    queryset = Produto.objects.get_queryset()
    success_url = reverse_lazy('home')


class UpdateProdutoView(UpdateView):
    prduto = Produto
    template_name = 'prod_update_form.html'
    fields = ['produto', 'quantidade', 'preco']
    success_url = reverse_lazy('home')


class DeleteProdutoView(DeleteView):
    prduto = Produto