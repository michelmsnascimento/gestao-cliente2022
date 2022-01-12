from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Produto
from .forms import ProdutoForm
from django.views.generic import View
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProdutoListView(ListView):
    model = Produto
    

@method_decorator(login_required, name='dispatch')
class ProdutoDetailView(DetailView):

    model = Produto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
        

@method_decorator(login_required, name='dispatch')
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['codigo','descricao','preco','photo']
    success_url = '/produtos/produto_list'

@method_decorator(login_required, name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['codigo','descricao','preco','photo']
    success_url = reverse_lazy ('produto_list_cbv')

@method_decorator(login_required, name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy ('produto_list_cbv')