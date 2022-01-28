from django.urls import path

import mlpred.views


## http://127.0.0.1:8000/main/
urlpatterns = [
    path('', mlpred.views.mlpred, name='mlpred'),
]