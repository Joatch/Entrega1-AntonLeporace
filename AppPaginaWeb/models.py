from django.db import models

class Libros(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)

class Juegos(models.Model):
    nombre = models.CharField(max_length=40)
    creador = models.CharField(max_length=40)

class Series(models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)

