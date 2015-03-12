#-*- coding: utf-8 -*-

from members.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from recipe.views import home
def connection(request):
    errors = {'connection': False}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe

            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                errors = {'connection': True}

    return home(request, errors)


def deconnection(request):
    errors = {'deconnection': False}

    logout(request)
    return home(request, errors)


