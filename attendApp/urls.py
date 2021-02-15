from django.contrib import admin
from django.urls import path, include
from attendApp import views

app_name= 'atdApp'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('ranking/', views.ranking, name='ranking'),
    path('curriculum/', views.curri, name='curri'),
    path('abrank/', views.abrank, name='difrank'),
    path('cusave/', views.custom_period, name='custom_save'),
    path('cudel/', views.custom_del, name='custom_del'),
    path('add/', views.add_attend, name='add'),
    path('text/', views.text, name='text'),

]
