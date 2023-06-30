from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso=Curso(nombre="Desarrollo Web",camada="19881")
    curso.save()
    documentoTexto=f"---->Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoTexto)
def inicio(request):
    return render (request,"inicio.html")
def cursos(request):
    return render (request, "cursos.html")
def profesores(request):
    return HttpResponse("Vista profesores")
def estudiantes(request):
    return HttpResponse("Vista estudiantes")
def entregables(request):
    return HttpResponse("Vista entregables")

