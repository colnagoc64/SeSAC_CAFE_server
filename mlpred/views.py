import json
from django.core import serializers
import pandas as pd
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import sklearn

# Create your views here.
from .web_data import near_cafe_db, near_subway_db, near_bus_db, gu_work_db, near_culture_db, area_cafe_db, \
    franchise_db, randomforest


def mlpred(request):
    print('------mlpred', request)

    return render(request, "mlpred/mlpred.html")


def search(request):
    print('------search API')
    try:
        context = json.loads(json.dumps(request.GET))
        area = float(context['area'])
        latLng_la = float(context['latLng_la'])
        latLng_ma = float(context['latLng_ma'])
        pric = float(context['pric'])
        target = []
        near_cafe = near_cafe_db(latLng_la, latLng_ma)
        near_bus = near_bus_db(latLng_la, latLng_ma)
        near_subway = near_subway_db(latLng_la, latLng_ma)
        gu_work = gu_work_db(latLng_la, latLng_ma)
        near_culture = near_culture_db(latLng_la, latLng_ma)
        area_cafe = area_cafe_db(latLng_la, latLng_ma)
        franchise = franchise_db(pric)


        target.extend(convertToList(area))
        target.extend(convertToList(near_cafe))
        target.extend(convertToList(near_bus))
        target.extend(convertToList(near_subway))
        target.extend(convertToList(gu_work))
        target.extend(convertToList(near_culture))
        target.extend(convertToList(area_cafe))
        target.extend(convertToList(franchise))



        target =pd.DataFrame(target)
        target = target.T
        pred = randomforest(target)
        pred = pred.astype(np.int32)
        ft_import = [near_cafe,near_bus[0],near_culture,area_cafe[0],area_cafe[1],gu_work[0]]

        return responseFormat(1,pred[0],ft_import)

    except ValueError as err:
        print(err)
        return responseFormat(0, 0,ft_import)


def convertToList(data):
    if type(data) is tuple:
        return list(data)
    else:
        return [data]

def responseFormat(errorCode,data,ft_import):
    pred = 0
    ft_import = ft_import
    if data == 1:
        pred = 1
    result = {
        "errorCode": errorCode,
        "data": pred,
        "ft_import": ft_import
    }
    return JsonResponse(result, safe=False)