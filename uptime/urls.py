from django.urls import path

from uptime.views import simple_uptime

app_name='uptime_calculator'

urlpatterns = [
    path('simple_uptime/', simple_uptime, name='simple-uptime')
]