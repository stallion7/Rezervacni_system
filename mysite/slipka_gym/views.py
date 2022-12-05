from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, "uvod.html")

def rezervace(request):
    return render(request, "rezervace.html")

def uvod(request):
    return render(request, "uvod_prihlaseny.html")