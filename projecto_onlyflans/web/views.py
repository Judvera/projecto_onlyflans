# Importacion de funciones para renderizar plantillas y redirigir.
from django.shortcuts import render, redirect
# Importacion del modelo Flan.
from .models import Flan
 # Importacion del formulario de contacto.
from .forms import ContactFormForm
# Importacion para redirigir respuestas HTTP.
from django.http import HttpResponseRedirect
# Importacion para mostrar mensajes de éxito o error a los usuarios.
from django.contrib import messages
# Improtacion para autenticación de usuarios.
from django.contrib.auth import authenticate, login, logout
# Importacion para restringir vistas a usuarios autenticados.
from django.contrib.auth.decorators import login_required

# Create your views here.
def indice(request):
    """ Funcion que renderiza la página de inicio.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página de inicio renderizada, mostrando solo los flanes públicos.
    """
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    """ Funcion que renderiza la página 'about.html' que contiene información general sobre el sitio.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página 'acerca' renderizada.
    """
    return render(request, 'about.html', {})

def bienvenido(request):
    """ Funcion que renderiza la página de bienvenida.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página de bienvenida renderizada, mostrando solo los flanes privados.
    """
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    """ Funcion que renderiza la página 'contact.html' con un formulario de contacto.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página de contacto, con el formulario correspondiente.
    """
    # validacion de solicitud.
    if request.method == 'POST':
        # Carga el formulario con datos POST.
        form = ContactFormForm(request.POST)
        # Verifica si el formulario es válido.
        if form.is_valid():
            # Guarda el formulario.
            form.save()
            # Redirige a la página de éxito.
            return HttpResponseRedirect('/exito')
    else:
        # Crea un formulario vacío.
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})

def exito(request):
    """ Funcion que renderiza la página 'exito.html' que indica que el formulario se envió correctamente.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página de exito.
    """
    return render(request, 'exito.html', {})

def login(request):
    """ Funcion que renderiza la página de inicio de sesión.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página de inicio de sesión.
    """
    # Validacion de solicitud.
    if request.method == 'POST':
        # Obtiene el nombre de usuario.
        username = request.POST.get('username')
        # Obtiene la contraseña.
        password = request.POST.get('password')
        # Autentica al usuario.
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Inicia sesión para el usuario autenticado.
            login(request, user)
            # Página a la que se redirige después del login.
            next_page = request.POST.get('next', 'welcome')
            # messages.success(request, '¡Inicio de sesión exitoso!')
            # Redirige a la página siguiente.
            return redirect(next_page)
        else:
            # Mensaje de error si falla la autenticación.
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def logout(request): 
    """ Funcion que renderiza y cierra sesión para el usuario autenticado y redirige a la página de inicio.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponseRedirect: Indica que, después de cerrar sesión, el usuario será redirigido a la página de inicio.
    """
    # messages.success(request, '¡Se ha cerrado sesión correctamente!')
    return redirect('/')

def explora(request):
    """ Renderiza la página 'explora.html', que muestra información sobre flanes y otros contenidos.

    Args:
        request (object): Instancia de la clase HttpRequest que representa la solicitud HTTP entrante al servidor Django.

    Returns:
        HttpResponse: Devuelve una respuesta HTTP que representa la página explora.
    """
    return render(request, 'explora.html')