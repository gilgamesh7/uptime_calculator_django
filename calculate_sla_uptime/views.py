from django.shortcuts import render

from calculate_sla_uptime.settings import logger

# Create your views here.
def uptime_sla(request):
    return render(request, 'uptime/simple_uptime.html')

