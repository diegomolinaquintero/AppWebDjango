from django.shortcuts import render
from .form import RegForm
# Create your views here.

def inicio  (request):
    form = RegForm()
    context = {
        "el_formulario": form
    }
    return render(request, "boletin/inicio.html",context)

