from django.shortcuts import render, redirect
from .forms import UsuarioRegistradoForm

def registro(request):
    if request.method == 'POST':
        form = UsuarioRegistradoForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('exito_registro')
    else:
        form = UsuarioRegistradoForm()
    return render(request, 'registro.html', {'form': form})

def base(request):
    return render(request, 'base.html')

def exito_registro(request):
    return render(request, 'exitoRegistro.html')