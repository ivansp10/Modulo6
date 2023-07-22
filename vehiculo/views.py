from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import VehiculoForm
from django.contrib import messages
from django.urls import reverse
def index(request):
    return render(request,'vehiculo/index.html')
# Create your views here.

def form_view(request):

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(form_view))
    else:
        form = VehiculoForm()
        context={'form':form}
        return render(request,'vehiculo/formulario.html',context)
