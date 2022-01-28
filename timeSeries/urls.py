from django.urls import path

import timeSeries.views

## http://127.0.0.1:8000/main/
urlpatterns = [
    path('', timeSeries.views.predict, name='timeSeries'),


]