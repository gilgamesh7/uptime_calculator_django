from django.shortcuts import render

from calculate_sla_uptime.settings import logger

import requests

# Create your views here.
def simple_sla(request):
    simple_sla_data = {}

    if 'simple_uptime_hours' in request.GET:
        try:
            hours_entered = request.GET['simple_uptime_hours']
            minutes_entered = request.GET['simple_uptime_minutes']
            seconds_entered = request.GET['simple_uptime_seconds']

            hours = 0 if hours_entered == '' else int(hours_entered)
            minutes = 0 if minutes_entered == '' else int(minutes_entered)
            seconds = 0 if seconds_entered == '' else int(seconds_entered)

            request_parameter = f"{hours}h{minutes}m{seconds}s"

            logger.info(f"Get Uptime for simple Uptime as input : {request_parameter}")

            with requests.Session() as session:
                response = session.get('https://get.uptime.is/api', params={'down': request_parameter})
                response.raise_for_status()

            simple_sla_data = response.json()
            logger.info(f"Simple SLA Data : {simple_sla_data}")
        except Exception as err:
            logger.error(f"Exception : {err}")

    return render(request, 'sla/simple_sla.html', {'simple_sla_data':simple_sla_data})

