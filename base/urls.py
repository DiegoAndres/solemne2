from django.conf.urls import url

from base import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^detalle/(?P<id>\d+)$', views.detalle_view, name='detalle'),
]
