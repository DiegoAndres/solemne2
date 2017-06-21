# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from base.models import Noticia


def index_view(request):
    noticias_destacada = Noticia.objects.filter(destacada = True).order_by('-fecha_publicacion').first()
    noticias            = Noticia.objects.filter(destacada = False).order_by('-fecha_publicacion')[:6]
    return render(request, 'index.html', {
        'noticias_destacada' : noticias_destacada,
        'noticias'           : noticias
    })


def detalle_view(request, id):
    noticia = get_object_or_404(Noticia, id = id)
    return render(request, 'detalle.html', {
        'noticia' : noticia
    })
