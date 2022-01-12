from django.contrib import admin
from django.urls import path, include
from vendas import urls as vendas_urls
from produtos import urls as produtos_urls
from clientes import urls as clientes_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls

urlpatterns = [
    path('', include(home_urls)),
    path('vendas/', include(vendas_urls)),
    path('produtos/', include(produtos_urls)),
    path('clientes/', include(clientes_urls)),
    path('login/', LoginView.as_view(), name="login"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Gestão de Clientes'
admin.site.index_title = 'Administração'   
admin.site.site_title = 'gestão clientes'   
