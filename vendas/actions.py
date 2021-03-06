from django.http.response import HttpResponseNotFound


def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)

    else:
        return HttpResponseNotFound('<h3>Sem Permissão</h3>')
    
nfe_emitida.short_description = 'NF-e emitida'

def nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

nfe_nao_emitida.short_description = 'NF-e nao emitida'