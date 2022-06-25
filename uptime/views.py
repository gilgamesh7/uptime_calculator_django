from django.shortcuts import render

import json

from calculate_sla_uptime.settings import logger

import requests

# Create your views here.
def simple_uptime(request):
    agreed_sla_level = {}

    if 'simple_sla' in request.GET:
        try:
            logger.info("Get Uptime for simple SLA % as input")
            simple_sla = request.GET['simple_sla']
            with requests.Session() as session:
                response = session.get('https://get.uptime.is/api', params={'sla': simple_sla})
                response.raise_for_status()

            agreed_sla_level = response.json()
        except Exception as err:
            logger.error(f"Exception : {err}")

    return render(request, 'uptime/simple_uptime.html', {'agreed_sla_level':agreed_sla_level})

