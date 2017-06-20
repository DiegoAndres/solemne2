# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Noticia(models.Model):
    """
        Modelo Noticia
    """
    titulo    = models.CharField( max_length = 100, verbose_name = u'titulo', help_text = "Titulo Noticia" )


class Categoria(models.Model):
    """
        Modelo Categoria
    """
    nombre    = models.CharField( max_length = 100, verbose_name = u'Nombre', help_text = "Nombre Categoria" )


class Publicacion(models.Model):
    """
        Modelo Noticia
    """
    noticia      = models.ForeignKey( Noticia, verbose_name = u'jerarquía' )
    creada       = models.DateTimeField( auto_now = True )
