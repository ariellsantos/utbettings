# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from forms import UserForm, LoginForm, UsuarioForm
from django.contrib.auth.models import  User
from .models import Usuario, Torneo, Evento, ResultadoEvento, Liga, Equipo
from roles import crear_rol

@login_required
def index(request):
    utcoins = request.user.usuario.monto
    print utcoins
    context = {
        'utcoins':utcoins
    }

    return render(request,"apuestas/index.html",context)

def login_user(request):
    if request.user.is_authenticated():
        return redirect("apuestas:index")
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    print "si se logeo"
                    return redirect("apuestas:index")
                else:
                    form = LoginForm()
                    return render(request, 'apuestas/usuarios/login.html', {'form': form})
        else:
            form = LoginForm()
        
            return render(request, 'apuestas/usuarios/login.html', {'form': form})
            
def logout_user(request):
    logout(request)
    return redirect('/')

def guardar_usuario(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if user_form.is_valid() and usuario_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = User.objects.create_user(username,email,password)
            user.first_name =  user_form.cleaned_data['first_name']

            usuario = usuario_form.save(commit=False)
            usuario.user = user

            usuario.save()
            user.save()

        return redirect("apuestas:index")

    
    elif request.method == "GET":
        if request.user.is_authenticated():
            return redirect("apuestas:index")
        else:    
            user_form = UserForm()
            form_usuario = UsuarioForm()
            return render(request, "apuestas/usuarios/crear_usuarios.html", {'user_form': user_form, 'usuario_form': form_usuario})

@login_required
def generar_rol(request, torneo):
    torneo = Torneo.objects.get(pk=torneo)
    crear_rol(torneo.liga.id, torneo.id)
    return redirect('apuestas:juegos', torneo=torneo.id)
@login_required
def torneos_apuestas(request):
    torneos = Torneo.objects.filter(rol=True)
    context = {
        'torneos': torneos
    }
    return render(request, 'apuestas/apuestas/torneos_apuestas.html', context)

@login_required
def torneos_sin_rol(request):
    torneos = Torneo.objects.filter(rol=False)
    context = {
        'torneos': torneos
    }
    return render(request,"apuestas/apuestas/torneos_sin_roles.html", context)

@login_required
def torneo(request, torneo):
    torneo = Torneo.objects.get(pk=torneo)
    juegos_torneo = Evento.objects.filter(torneo=torneo)
    context = {
        'juegos': juegos_torneo,
        'torneo': torneo,
    }
    return render(request, 'apuestas/apuestas/juegos_torneo.html',context)