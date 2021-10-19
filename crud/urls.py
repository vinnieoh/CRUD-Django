from django.urls import path

from .views import HomeView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-produto/', CreateProdutoView.as_view(), name='produto_create'),
    path('<int:pk>/update-produto/', UpdateProdutoView.as_view(), name='produto_update'),
    path('<int:pk>/delete-produto/', DeleteProdutoView.as_view(), name='produto_delete'),
]