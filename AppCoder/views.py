from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


# Create your views here.
def curso(self):
    curso=Curso(nombre="Desarrollo Web",camada="19881")
    curso.save()
    documentoTexto=f"---->Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoTexto)
def inicio(request):
    return render (request,"inicio.html")
def entregables(request):
    return render (request, "entregables.html")
def cursos(request):
      if request.method == "POST":
          miFormulario=CursoFormulario(request.POST) #dodne llega la información del html
          print(miFormulario)
          if miFormulario.is_valid():
              informacion = miFormulario.cleaned_data
              curso = Curso(nombre= informacion['nombre'],camada=informacion['camada'])
              curso.save()
              return render(request, 'inicio.html')
      else:
          miFormulario=CursoFormulario()
      return render(request, "cursos.html",{"miFormulario":miFormulario})

def profesores(request):
    if request.method == "POST":
        miFormulario=ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            profesor=Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],profesion=informacion['profesion'])
            profesor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario=ProfesorFormulario()
    return render(request, 'profesores.html',{'miFormulario':miFormulario})

def estudiantes(request):
    if request.method == "POST":
        miFormulario=EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            estudiante=Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render (request, 'inicio.html')
    else:
        miFormulario=EstudianteFormulario()
    return render (request, 'estudiantes.html',{'miFormulario':miFormulario})

def entregables(request):
    if request.method=="POST":
        miFormulario=EntregableFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            entregable=Entregable(nombre=informacion['nombre'],fecha_entrega=informacion['fecha_entrega'],entregado=informacion['entregado'])
            entregable.save()
            return render (request, 'inicio.html')
    else:
        miFormulario=EntregableFormulario()
    return render(request, 'entregables.html',{'miFormulario':miFormulario})
    
            
def busquedaCamada(request):
    return render(request, 'busquedaCamada.html')
def buscar(request):
    if request.GET['camada']:

        #respuesta=f"Estoy buscando la Camada numero: {request.GET['camada']}"
        camada=request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, 'inicio.html',{'cursos':cursos, 'camada':camada})
    else:
        respuesta= "No enviaste datos."
    
    #return HttpResponse(respuesta)
    return render (request, 'inicio.html',{'respuesta':respuesta})

def leerProfesores(request):
    profesores= Profesor.objects.all()
    contexto={"profesores":profesores}
    return render (request, "leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):
 
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
 
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
 
    contexto = {"profesores": profesores}
 
    return render(request, "leerProfesores.html", contexto)

def editarProfesor (request, profesor_nombre):
    profesor=Profesor.objects.get(nombre=profesor_nombre)
    if request.method == "POST":
        miFormulario=ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            profesor.nombre=informacion['nombre']
            profesor.apellido=informacion['apellido']
            profesor.email=informacion['email']
            profesor.profesion=informacion['profesion']

            profesor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario=ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
    return render(request, 'editarProfesor.html',{'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})

class CursoList(ListView):
    model = Curso
    template_name: 'cursos_list.html'

class CursoDetalle(DetailView):
    model=Curso
    template_name='curso_detalle.html'

class CursoCreacion(CreateView):
    model=Curso
    success_url='/AppCoder/curso/list'
    fields=['nombre','camada']

class CursoUpdate(UpdateView):
    model=Curso
    success_url='/AppCoder/curso/list'
    fields=['nombre','camada']

class CursoDelete(DeleteView):
    model=Curso
    success_url='/AppCoder/curso/list'