from django.shortcuts import render, redirect
from .forms import UsuarioRegistradoForm
from django.contrib.auth import login #para crear cookie de logueo

def registro(request):
    if request.method == 'POST': #si aprieto registrar...
        form = UsuarioRegistradoForm(request.POST) #creo un formulario con los datos recibidos
        if form.is_valid(): #compruebo validaciones def clean_... hechas en el forms
            usuario = form.save()
            login(request, usuario)
            return redirect('exito_registro')
    else:
        form = UsuarioRegistradoForm() #retorno formulario con campos fallidos vacíos
    return render(request, 'registro.html', {'form': form})

def base(request):
    return render(request, 'base.html')

def exito_registro(request):
    return render(request, 'exitoRegistro.html')