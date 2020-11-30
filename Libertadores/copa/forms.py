from django.shortcuts import render
from . models import Usuario
from . models import Comentario
from django.views import generic


from django import forms



class ComentarioForm(forms.Form):
    rut1 = forms.CharField()
    nombre = forms.CharField()
    descripcion = forms.CharField()