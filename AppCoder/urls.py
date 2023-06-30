from django.urls import path
from AppCoder import views


urlpatterns = [
    path("",views.inicio),
    path("cursos",views.cursos, name="Cursos"),
    path("profesores",views.profesores, name="Profesores"),
    path("cursos",views.estudiantes, name="Estudiantes"),
    path("cursos",views.entregables, name="Entregables"),
    
]