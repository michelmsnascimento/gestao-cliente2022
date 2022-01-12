from django.contrib import admin
from .models import Person, Documento



class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'photo')
        })
    )
    
    list_filter = ('age', 'salary')
    list_display = ('doc', 'first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
    search_fields = ('id', 'first_name')
    
    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
    
    tem_foto.short_description = 'Possui Foto'
    


class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)

