from django.db import models


from django.contrib.auth.models import AbstractUser

def upload_location(instance, filename):
    #Esta función guarda las imágenes de los usuarios en media_cdn/<id_usuario>
    return "usuarios/%s/%s" %(instance.id, filename)

# Create your models here.
class Usuario(AbstractUser):
    fecha_nac = models.DateField(blank=True,null=True)
    imagen = models.ImageField(upload_to=upload_location, blank=True,null=True)
    rol = models.CharField(max_length=1,blank=True,null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Prueba(models.Model):
    #idHorario = models.AutoField(primary_key = True)
    dia = models.CharField(max_length=9)
    fecha_inicio = models.TimeField()
    fecha_fin = models.TimeField()




