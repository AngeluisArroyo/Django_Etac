from django.urls import path
from . import views

urlpatterns = [
    path('',views.grafica_view, name= 'grafica_view'),
]
