from django.urls import path
from . import views

app_name = 'managedata'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/v1/person-ls', views.PersonListAPIView.as_view(),
         name="person_list_api"),
]
