from django.db import models
from django.conf import settings

class Career(models.Model):
    name = models.CharField("nombre", max_length=50, blank=False, null=True)
    
    class Meta:
        verbose_name = "carrera"
        verbose_name_plural = "carreras"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField("nombre", max_length=100, blank=False, null=True)

    class Meta:
        verbose_name = "localidad"
        verbose_name_plural = "localidades"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField("nombre", max_length=50, blank=False, null=True)
    last_name = models.CharField("apellido",max_length=50,blank=False,null=True)
    addres = models.CharField("domicilio",max_length=100,blank=False,null=True)
    number_phone = models.CharField("numero de telefono", max_length=25,blank=False,null=True)
    id_location_connect = models.ForeignKey(Location,on_delete=models.PROTECT,verbose_name="localidad",
                                            related_name="Teacher_id_location_connect", null=True, blank=False)

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"

    def __str__(self):
        return " %s %s " % (self.last_name, self.name)


class Matter(models.Model):
    name = models.CharField("nombre", max_length=50, blank=False, null=True)
    id_career = models.ForeignKey(Career,on_delete=models.PROTECT,verbose_name="carrera",
                                        related_name="Matter_id_career",null=True,blank=False)
    id_teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT,verbose_name="profesor",
                                        related_name="Matter_id_teacher",null=True,blank=False)

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,verbose_name="usuario",
                                        related_name="user",null=True,blank=False)
    title = models.CharField(max_length=255)
    content = models.TextField()