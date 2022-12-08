from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, "uvod.html")

@login_required
def rezervace(request):
    return render(request, "rezervace.html")

@login_required
def uvod(request):
    return render(request, "uvod_prihlaseny.html")