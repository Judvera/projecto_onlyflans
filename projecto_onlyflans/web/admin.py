from django.contrib import admin
# Importa los modelos Flan y ContactForm desde el módulo actual.
from .models import Flan, ContactForm

# Registra el modelo Flan en el panel de administración.
# Esto permite gestionar instancias de Flan a través de la interfaz de administración de Django.
admin.site.register(Flan)

# Registra el modelo ContactForm en el panel de administración.
# Con esto, se puede gestionar instancias del formulario de contacto desde la interfaz de administración.
admin.site.register(ContactForm)