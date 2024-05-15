from django.shortcuts import render, redirect
from .forms import UsuarioRegistradoForm

def registro(request):
    if request.method == 'POST': #si aprieto registrar...
        form = UsuarioRegistradoForm(request.POST) #creo un formulario con los datos recibidos
        if form.is_valid(): #compruebo validaciones def clean_... hechas en el forms
            usuario = form.save()
            return redirect('exito_registro')
    else:
        form = UsuarioRegistradoForm() #retorno formulario con campos fallidos vacíos
    return render(request, 'registro.html', {'form': form})

def base(request):
    return render(request, 'base.html')

def exito_registro(request):
    return render(request, 'exitoRegistro.html')