from django.shortcuts import render
from . models import Usuario
from . models import Comentario
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    num_Usuarios = Usuario.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_usuarios ': num_Usuarios }
    )

def galeria(request):
    

    return render(
        request,
        'galeria.html',
       
    )

   
class UsuarioDetailView(generic.DetailView):
    model = Usuario

class UsuarioListView(generic.ListView):
    model = Usuario


class UsuarioCreate(CreateView):
    model= Usuario
    fields= '__all__'

class UsuarioUpdate(UpdateView):
    model= Usuario
    fields= ['rut','first_name','last_name','edad','equipo','Direccion']

class UsuarioDelete(DeleteView):
    model= Usuario
    success_url = reverse_lazy('index')



class ComentarioDetailView(generic.DetailView):
    model = Comentario

class ComentarioListView(generic.ListView):
    model = Comentario

class ComentarioCreate(CreateView):
    model= Comentario
    fields= '__all__'
    

class ComentarioUpdate(UpdateView):
    model= Comentario
    fields= ['rut1','nombre','descripcion']

class ComentarioDelete(DeleteView):
    model= Comentario
    success_url = reverse_lazy('index')

