from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.db import models
from WebAdminRadio import models as adminModels


from django.contrib.auth.models import AbstractUser

def upload_location(instance, filename):
    #Esta función guarda las imágenes de los usuarios en media_cdn/<id_usuario>
    return "usuarios/%s/%s" %(instance.slug, filename)

# Create your models here.
class Usuario(AbstractUser):
    fecha_nac = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to=upload_location, blank=True, null=True)
    rol = models.CharField(max_length=1, blank=True, null=True)
    biografia = models.CharField(max_length=500, blank=True, null=True)
    apodo = models.CharField(max_length=50, blank=True, null=True)
    hobbies = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    #obtiene las redes sociales del Usuario (Locutor)
    def get_redes_sociales(self):
        return adminModels.RedSocial_usuario.objects.filter(idUsuario=self.pk).values()

class Prueba(models.Model):
    #idHorario = models.AutoField(primary_key = True)
    dia = models.CharField(max_length=9)
    fecha_inicio = models.TimeField()
    fecha_fin = models.TimeField()

def create_slug(instance, sender, new_slug=None):
    slug = slugify(instance.username)
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, sender, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Usuario)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance, sender)