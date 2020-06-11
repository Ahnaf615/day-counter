from django.urls import path
from . import views

urlpatterns = [
    path('', views.bday, name='bday')
]