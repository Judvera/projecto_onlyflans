from django import forms
# Importa el modelo ContactForm del módulo actual para usarlo en el formulario.
from .models import ContactForm

# Define un formulario basado en el modelo ContactForm.
class ContactFormForm(forms.ModelForm):
    """ Este formulario se basa en el modelo `ContactForm`. Se utiliza para capturar la dirección
    de correo electrónico del cliente, su nombre y el mensaje que desean enviar.
    """
    class Meta:
        """ Metadatos para el formulario ContactFormForm.
        La clase `Meta` define la configuración del formulario para el modelo `ContactForm`.
        Especifica qué modelo se utiliza, qué campos se incluyen en el formulario y las
        etiquetas personalizadas para cada campo.
        
        Args:
            model (Model): El modelo de Django en el que se basa el formulario.
            fields (list): Lista de nombres de campos que se incluirán en el formulario.
            labels (dict): Diccionario con las etiquetas personalizadas para cada campo.
        """
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo',
            'customer_name': 'Nombre',
            'message': 'Mensaje'
        }