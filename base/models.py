# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField


class Categoria(models.Model):
    """
        Modelo Categoria
    """
    nombre    = models.CharField( max_length = 100, verbose_name = u'Nombre', help_text = "Nombre Categoria" )

    def __unicode__( self ):
        return self.nombre


class Noticia(models.Model):
    """
        Modelo Noticia
    """
    titulo    = models.CharField( max_length = 100, verbose_name = u'titulo', help_text = "Titulo Noticia" )
    contenido = models.CharField( max_length = 1000, verbose_name = u'contenido', help_text = "Contenido" )
    imagen    = ImageField(upload_to = 'imagenes/' )
    categoria = models.ForeignKey( Categoria, verbose_name = u'categoria' )
    destacada = models.BooleanField(default = False)
    fecha_publicacion  = models.DateTimeField( auto_now_add = True )
    fecha_modificacion = models.DateTimeField( auto_now = True )

    def __unicode__( self ):
        return self.titulo
