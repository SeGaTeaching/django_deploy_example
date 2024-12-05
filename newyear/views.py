from django.shortcuts import render
import datetime

# Create your views here.
def newyear(request):
    now = datetime.datetime.now()
    yes_or_no = now.month == 1 and now.day == 1
    return render(request, 'newyear/newyear.html', {'newyear': yes_or_no, 'today': now})