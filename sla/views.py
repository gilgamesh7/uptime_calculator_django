from django.shortcuts import render

from calculate_sla_uptime.settings import logger

import requests

# Create your views here.
def simple_sla(request):
    simple_sla_data = {}

    # if 'simple_uptime' in request.GET:
    #     try:
    #         logger.info("Get SLA for simple Uptime as input")
    #         simple_sla = request.GET['simple_uptime']
    #         with requests.Session() as session:
    #             response = session.get('https://get.uptime.is/api', params={'sla': simple_sla})
    #             response.raise_for_status()

    #         simple_downtime_data = response.json()
    #     except Exception as err:
    #         logger.error(f"Exception : {err}")

    return render(request, 'sla/simple_sla.html', {'simple_sla_data':simple_sla_data})

