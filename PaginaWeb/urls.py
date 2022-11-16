"""PaginaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppPaginaWeb.views import *
from AppPaginaWeb.admin import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='Index'),
    path('crear_juego', crear_juego, name='Crear Juego'),
    path('crear_libro', crear_libro, name='Crear Libro'),
    path('crear_serie', crear_serie, name='Crear Serie'),
    path('aqwerq', aviso, name= 'Aviso'),
    path('buscar_libro', buscar_libro, name='Buscar Libro'),
    path('buscar_serie', buscar_serie, name='Buscar Serie'),
    path('buscar_juego', buscar_juego, name='Buscar Juego')
]
