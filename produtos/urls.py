from django.urls import path
from .views import ProdutoListView
from .views import ProdutoDetailView
from .views import ProdutoCreateView
from .views import ProdutoUpdateView
from .views import ProdutoDeleteView


urlpatterns = [
    path('produto_list/', ProdutoListView.as_view(), name="produto_list_cbv"),
    path('produto_detail/<int:pk>/', ProdutoDetailView.as_view(), name="produto_detail_cbv"),
    path('produto_update/<int:pk>/', ProdutoUpdateView.as_view(), name="produto_update_cbv"),
    path('produto_delete/<int:pk>/', ProdutoDeleteView.as_view(), name="produto_delete_cbv"),
    path('produto_create/', ProdutoCreateView.as_view(), name="produto_create_cbv"),
]