from django.shortcuts import render

from .models import Flan

from django.http import HttpResponseRedirect

from .forms import ContactFormModelForm

from django.contrib.auth.decorators import login_required
 
@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
 
    return render(
        request,
        'welcome.html',
        {
            'private_flans': private_flans
        }
    )


def indice(request):
    public_flans = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'public_flans': public_flans})


def acerca(request):
    return render(request, 'about.html', {})


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

def promociones(request):
    return render(request, 'promociones.html', {})