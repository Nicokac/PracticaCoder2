from django.urls import path
from .views import crea_curso, lista_cursos, profesores, cursos, estudiantes, entregables, inicio

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_cursos),
    path("", inicio),
    path('profesores/', profesores, name="Profesores"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),

]
