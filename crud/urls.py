from django.urls import path, include
from .views import helloAPI, showRoutine

urlpatterns = [
     path("hello/", helloAPI),
     path("",showRoutine)
]
