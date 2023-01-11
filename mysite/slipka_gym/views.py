from typing import List

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Trenink
from .forms import TreninkForm
from .forms import PrihlaseniForm

def index(request):
    return render(request, "uvod.html")

@login_required
def rezervace(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    trenink_list = Trenink.objects.all()
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    #get current year, month, day
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    #get current time
    time = now.strftime('%H:%M')
    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, "rezervace.html",
                  {"current_year": current_year,
                   "current_month": current_month,
                   "current_day": current_day,
                   "year": year,
                   "month": month,
                   "month_number": month_number,
                   "cal": cal,
                   "time": time,
                   'trenink_list': trenink_list
                   })

@login_required
def uvod(request):
    return render(request, "uvod_prihlaseny.html")

@login_required
def add_trenink(request):
    submitted = False
    if request.method == "POST":
        form = TreninkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../rezervace?submitted=True')
    else:
        form = TreninkForm
        if 'submitted' in request.GET:
            submitted = True

    return  render(request, "trenink.html", {'form': form, 'submitted': submitted})

@login_required
def prihlaseni_trenink(request, trenink_id):
    trenink = Trenink.objects.get(pk=trenink_id)
    form = PrihlaseniForm(request.POST or None, instance=trenink)
    if form.is_valid():
        form.save()
        return redirect('rezervace')
    return render(request, "prihlaseni_trenink.html", {'trenink': trenink, 'form': form})

@login_required
def update_trenink(request, trenink_id):
    trenink = Trenink.objects.get(pk=trenink_id)
    form = TreninkForm(request.POST or None, instance=trenink)
    if form.is_valid():
        form.save()
        return redirect('rezervace')
    return render(request, "update_trenink.html", {'trenink': trenink, 'form': form})

@login_required
def delete_trenink(request, trenink_id):
    trenink = Trenink.objects.get(pk=trenink_id)
    trenink.delete()
    return redirect('rezervace')

def show_trenink(request, trenink_id):
    trenink = Trenink.objects.get(pk=trenink_id)
    return render(request, "show_trenink.html",
                  {'trenink': trenink})

def seznam_treninku(request):
    seznam_treninku = Trenink.objects.all()
    return render(request, "trenink_list.html",
                  {'seznam_treninku': seznam_treninku})


