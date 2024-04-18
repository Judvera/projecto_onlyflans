from django.db import models
from django.utils.text import slugify
from uuid import uuid4

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid4, editable=False, unique=True, verbose_name="UUID del Flan")
    name = models.CharField(max_length=64, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    image_url = models.ImageField(upload_to='img', verbose_name="Imagen")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    is_private = models.BooleanField(default=False, verbose_name="¿Es Privado?")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Flan, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Flan"
        verbose_name_plural = "Flanes"

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.customer_email}"
