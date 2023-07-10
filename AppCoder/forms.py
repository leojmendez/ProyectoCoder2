from django import forms
 
class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()
    
class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    fecha_entrega=forms.DateField()
    entregado=forms.BooleanField()