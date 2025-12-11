from django.urls import path
from .views import home, buscar

urlpatterns = [
    path("", home, name="home"),
    path("buscar/", buscar, name="buscar"),
]
