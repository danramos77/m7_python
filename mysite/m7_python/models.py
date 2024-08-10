from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    
class Tipo_inmueble(models.Model):
    tipo_inmueble = models.TextField()

class Comuna(models.Model):
    comuna = models.TextField()

class Region(models.Model):
    region = models.TextField()

class Tipo_user(models.Model):
    tipo_user = models.TextField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_tipo_user = models.ForeignKey('m7_python.Tipo_user', on_delete=models.CASCADE, null=True)
    rut =  models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.TextField()

class Inmuebles(models.Model):
    id_user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)
    id_tipo_inmueble = models.ForeignKey('m7_python.Tipo_inmueble', on_delete=models.CASCADE, null=True)
    id_comuna = models.ForeignKey('m7_python.Comuna', on_delete=models.CASCADE, null=True)
    id_region = models.ForeignKey('m7_python.region', on_delete=models.CASCADE, null=True)
    nombre_inmueble = models.TextField()
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    m2_construido = models.FloatField(default=0)
    numero_banos = models.IntegerField(default=0)
    numero_hab = models.IntegerField(default=0)
    direccion = models.CharField(max_length=200) 
    m2_terreno = models.FloatField(default=0)    #agregado
    numero_est = models.IntegerField(default=0)   #agregado
   
    #tipo_inmueble = models.CharField(max_length=10, null=False, blank=False)
    #precio_mensual = models.IntegerField(null=True, blank=True)
    #estado = models.BooleanField(null=False, blank=True )
   
    #numero_est = models.IntegerField(null=True, blank=True)
    #lat = models.FloatField(verbose_name='Latitud')
    #lng = models.FloatField(verbose_name='Longitud')

    #class Meta:
     #   verbose_name = 'Ubicacion'
      #  verbose_name_plural = 'Ubicaciones'
       # ordering = ['name']

    #def __str__(self) -> str:
    #    return self.name
    

    
    







