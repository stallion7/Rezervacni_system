from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, "uvod.html")