from django.conf.urls import url
from . import views

urlpatterns = [
    #url("", views.index, name="load index page")
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^entertainment', views.entertainment, name='entertainment'),
    url(r'^art', views.art, name='art'),
    url(r'^comedy', views.comedy, name='comedy'),
    url(r'^admin', views.admin, name='admin'),
    url(r'^workshop', views.workshop, name='workshop'),
    url(r'^sport', views.sport, name='sport'),
    url(r'^conference', views.conference, name='conference'),

    #url(r'^base/$', views.base, name='base'),
]