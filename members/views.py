#-*- coding: utf-8 -*-

from django.shortcuts import render
from members.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def connection(request):
    errorLogin = 0

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe

            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                errorLogin = 1
    else:
        form = LoginForm()

    return render(request, 'recipe/list.html', {'errorLogin': errorLogin})


def deconnection(request):
    logout(request)
    return render(request, 'recipe/list.html', {'errorDeconnect': 0})


