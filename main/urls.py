from django.urls import path

import main.views

## http://127.0.0.1:8000/main/
urlpatterns = [
    path('', main.views.index, name='index'),
    path('chart', main.views.chart, name='chart'),
]