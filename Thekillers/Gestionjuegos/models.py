from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=35)
    apellido= models.CharField(max_length=35)
    correo = models.CharField(max_length=35)

    def nombreCompleto(self):
        cadena= "{0} {1}"
        return cadena.format(self.nombre,self.apellido)

    def __str__(self):
        return self.nombreCompleto()

class consola(models.Model):
    nombre = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)

    #lo que retorna la clase
    
    def __str__(self):
        return self.nombre


class room(models.Model):
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    fechaLanzamiento = models.CharField(max_length=4)
    desarrolladora = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    especificacion = models.CharField(max_length=255)
    consola = models.ForeignKey(consola, on_delete=models.CASCADE)

    def juegoMasConsola(self):
        cadena= "{0} ({1})"
        return cadena.format(self.nombre,self.consola.marca)

    def __str__(self):
        return self.juegoMasConsola()