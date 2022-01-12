from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.


@login_required
def persons_list(request):
    persons = Person.objects.all()
    footer_message = "Gestão Clientes 2021"
    return render(request, 'person.html', {'persons': persons, 'footer_message': footer_message})

@login_required
def products_list(request):
    produtos = Produto.objects.all()
    footer_message = "Gestão Produtos 2021"
    return render(request, 'produto.html', {'produtos': produtos, 'footer_message': footer_message})



@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
       return HttpResponse('Não Autorizado')
    

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request,'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request,'person_delete_confirm.html', {'person': person})

class PersonListView(ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'voce ja acessou hoje'

        return context
    
class PersonDetailView(DetailView):
    model = Person
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PersonCreateView(CreateView):
    model = Person
    fields = ['first_name','last_name','age','salary','bio','photo']
    success_url = '/clientes/person_list'

class PersonUpdateView(UpdateView):
    model = Person
    fields = ['first_name','last_name','age','salary','bio','photo']
    success_url = reverse_lazy ('person_list')

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy ('person_list')
    
