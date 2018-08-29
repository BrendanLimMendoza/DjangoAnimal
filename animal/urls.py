from django.contrib import admin
from . import views
from django.urls import path

app_name = 'animal'

urlpatterns = [
    path('^$', views.index_view.as_view(), name="index"),
    path('^create/$', views.CreateAnimalView.as_view(), name="create"),


    path('^(?P<pk>[0-9]+)/$', views.detail_view.as_view(), name='detail'),

    path('animal/add/$', views.create_animal.as_view(), name='create-animal'),

    #edit animal url
    path('animal/(?P<pk>[0-9]+)/$', views.UpdateAnimal.as_view(), name='update-animal'),

    path('animal/(?P<pk>[0-9]+)/delete/$', views.DeleteAnimal.as_view(), name='delete-animal'),
]