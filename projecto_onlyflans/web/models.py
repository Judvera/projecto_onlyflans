from django.db import models
# Importa la función slugify para generar slugs a partir de texto.
from django.utils.text import slugify
# Importa uuid4 para generar identificadores únicos.
from uuid import uuid4

class Flan(models.Model):
    """ Modelo para flanes.

    Args:
        models (class): Es la clase base de Django para definir modelos, que actúan como representación lógica de tablas de base de datos.
    """
    # Campo UUID para identificar el Flan de forma única.
    flan_uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name="UUID del Flan")
    
    # Campo para el nombre del Flan, con un máximo de 64 caracteres.
    name = models.CharField(max_length=64, verbose_name="Nombre")
    
    # Campo para la descripción del Flan.
    description = models.TextField(verbose_name="Descripción")
    
    # Campo para el precio del Flan, con un máximo de 7 dígitos y sin decimales.
    price = models.DecimalField(max_digits=7, decimal_places=0, verbose_name="Precio", default=0)
    
    # Campo para almacenar la imagen del Flan, con un directorio de carga específico.
    image_url = models.ImageField(upload_to='img', verbose_name="Imagen")
    
    # Campo para el slug del Flan, asegurando unicidad.
    slug = models.SlugField(unique=True, verbose_name="Slug")
    
    # Campo booleano para indicar si el Flan es privado.
    is_private = models.BooleanField(default=False, verbose_name="¿Es Privado?")
    
    def formatted_price(self):
        """
        Devuelve el precio del Flan formateado.
        """
        return f"${self.price:,.0f}".replace(",", ".")

    def save(self, *args, **kwargs):
        """ Sobrescribe el método save para generar automáticamente un slug a partir del nombre
        si no está definido antes de guardar.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super(Flan, self).save(*args, **kwargs)

    def __str__(self):
        """ 
        Retorna el nombre del Flan.
        """
        return self.name

    class Meta:
        # Nombre para el modelo en singular.
        verbose_name = "Flan"
        # Nombre para el modelo en plural.
        verbose_name_plural = "Flanes"

class ContactForm(models.Model):
    """ Modelo para flanes.

    Args:
        models (class): Es la clase base de Django para definir modelos, que actúan como representación lógica de tablas de base de datos.
    """
    # UUID único para identificar el formulario de contacto.
    contact_form_uuid = models.UUIDField(default=uuid4, editable=False)
    
    # Campo para el correo electrónico del cliente.
    customer_email = models.EmailField()
    
    # Campo para el nombre del cliente, con un máximo de 64 caracteres.
    customer_name = models.CharField(max_length=64)
    
    # Campo para el mensaje del cliente.
    message = models.TextField()

    def __str__(self):
        """ 
        Retorna una representación legible del formulario de contacto, usando el nombre y el correo electrónico del cliente.
        """
        return f"{self.customer_name} - {self.customer_email}"
