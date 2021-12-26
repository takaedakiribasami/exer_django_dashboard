from django.urls import path
from . import views

app_name = 'managedata'
urlpatterns = [
    path('', views.index, name='index'),
]
