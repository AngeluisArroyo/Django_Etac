from django.urls import path
from . import views

urlpatterns = [
    path('',views.grafica_view, name= 'grafica_view'),
    path('graficas_2/',views.grafica_view_2, name= 'grafica_view_2'),
    path('graficas_3/',views.grafica_view_3, name= 'grafica_view_3')
]
