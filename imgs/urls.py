
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('buscar/<valor>',views.valor,name="valor"),

]
