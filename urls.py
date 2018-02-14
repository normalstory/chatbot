from django.conf.urls import url 
from . import views 

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^gongju$', views.gongju, name='gongju'),
    url(r'^chunan$', views.chunan, name='chunan'),
    url(r'^sejong$', views.sejong, name='sejong'), 
]
