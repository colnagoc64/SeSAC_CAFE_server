from django.urls import path

import main.views

## http://127.0.0.1:8000/main/
urlpatterns = [
    path('', main.views.index, name='index'),
    path('guCount', main.views.guCount, name='guCount'),
    path('logout', main.views.logout, name='logout'),
    path('chart', main.views.chart, name='chart'),
    path('map', main.views.map, name='map'),
    path('map2', main.views.map2, name='map2'),
    path('api/chart1/data', main.views.chartData.as_view(), name="chartData"),

    # path('/result', main.views.result_detail, name='result_detail'),
]