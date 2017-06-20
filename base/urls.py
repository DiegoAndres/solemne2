from django.conf.urls import url
from base import views

urlpatterns = [
    url(r'^index/$', views.index_view, name='index'),
]
