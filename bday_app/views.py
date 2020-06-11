from django.shortcuts import render
from .script_main import time_calc


# Create your views here.


def bday(request):
    if request.method == 'POST':
        try:
            month = int(request.POST['month'])
            day = int(request.POST['day'])
            context = time_calc(month, day)
            return render(request, 'bday_app/home.html', {'context': context})
        except Exception:
            error = 'input error'
            return render(request, 'bday_app/home.html', {'error': error})
    return render(request, 'bday_app/home.html')
