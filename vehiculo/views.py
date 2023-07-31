from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import VehiculoForm,UserRegisterForm
from .models import Vehiculo
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


@login_required(login_url='/login/')
def index(request):
    return render(request,'vehiculo/index.html')
# Create your views here.

@login_required(login_url='/login/')
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
@login_required(login_url='/login/')
def listar_view(request):
    vehiculos=Vehiculo.objects.all()
    context = {'vehiculos':vehiculos}
    return render(request,'vehiculo/lista_vehiculos.html',context)

def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo= Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type
            )
            user.user_permissions.add(visualizar_catalogo)
            login(request,user)
            messages.success(request,"Se ha registrado satisfactoriamente")
            return HttpResponseRedirect("/")
        else:
            messages.error(request,"Registro inválido")
        return HttpResponseRedirect("/register/")
    form=UserRegisterForm()
    context={'form':form}
    return render(request,'vehiculo/register.html',context)



def login_view(request):
    if request.method =="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password') 
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                messages.info(request,f"Iniciaste sesión como {username}. ")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'Nombre de usuario y/o contraseña incorrecta')
                return HttpResponseRedirect('/login/')
        else:
            messages.error(request,'Nombre de usuario y/o contraseña incorrecta')
            return HttpResponseRedirect('/login/')    
    form=AuthenticationForm()
    context = {'form':form}
    return render(request,'vehiculo/login.html',context)

def logout_view(request):
    logout(request)
    messages.info(request,"se ha cerrado la sesión correctamente")
    return HttpResponseRedirect('/login/')