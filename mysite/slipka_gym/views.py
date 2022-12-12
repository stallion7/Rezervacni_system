from typing import List

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def index(request):
    return render(request, "uvod.html")

@login_required
def rezervace(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
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
                   })

@login_required
def uvod(request):
    return render(request, "uvod_prihlaseny.html")