from django.urls import path
# importar todas las views
from .import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index_product'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    path('logout/', views.custom_logout, name='logout'),
    path('productos-ofertas/', views.productos_ofertas, name='productos_ofertas'),
    path('create/', views.create, name='create_product'),
    path('sale/', views.sale, name='sale_product'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    

    
    # Otras URLs...
]