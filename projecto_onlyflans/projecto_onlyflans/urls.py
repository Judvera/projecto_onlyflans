"""
URL configuration for projecto_onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Importacion de las vistas del proyecto.
from web.views import indice, acerca, bienvenido, contacto, exito, explora, login
# Para acceder a las configuraciones del proyecto. (Para uso del directorio MEDIA)
from django.conf import settings
# Para servir archivos estáticos en desarrollo. (Para uso del directorio MEDIA)
from django.conf.urls.static import static
# Importa vistas predeterminadas de autenticación.
from django.contrib.auth import views as auth_views

# Se definen las rutas de URL para el proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name='indice'),
    path('acerca', acerca, name='acerca'),
    path('bienvenido', bienvenido, name='bienvenido'),
    path('contacto', contacto, name='contacto'),
    path('exito', exito, name='exito'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('explora', explora, name='explora'),
]

# Si DEBUG es TRUE, añade rutas para servir archivos multimedia estáticos.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   

