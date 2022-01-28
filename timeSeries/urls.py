from django.urls import path

import timeseries.views

## http://127.0.0.1:8000/main/
urlpatterns = [
    path('', timeseries.views.timeseries, name='timeseries'),

]