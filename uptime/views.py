from django.shortcuts import render

# Create your views here.
def simple_uptime(request):
    agreed_sla_level = {}

    agreed_sla_level = 0

    return render(request, 'uptime/simple_uptime.html', {'agreed_sla_level': agreed_sla_level})