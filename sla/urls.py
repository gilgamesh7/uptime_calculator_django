from django.urls import path

from sla.views import simple_sla

app_name='sla_calculator'

urlpatterns = [
    path('simple_sla/', simple_sla, name='simple-sla')
]