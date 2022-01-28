import csv

from django.shortcuts import render
# Create your views here.
from main.models import CafeStatus


def index(request):
    qs = CafeStatus.objects.all()
    datas = qs.values()
    lat = []
    lng = []
    gu = []
    cafe_name = []
    print(datas[0]['cafe_name'])

    for i in datas:
        if i['business'] == 1:
            lat.append(i['lat'])
            lng.append(i['lng'])
            gu.append(i['gu'])
            cafe_name.append(i['cafe_name'])

    context = {
        "gu": gu,
        "lat": lat,
        "lng": lng,
        "cafe_name": cafe_name,
    }

    return render(request, 'main/index.html', context)

def chart(request):
    # try:
    #     queryset = CafeCount.objects.all()
    #     datas = queryset.values()
    #
    #     result = []
    #     for list in datas:
    #         result.append(list)
    #
    # except:
    #     print("쿼리 실행 실패")

    return render(request, 'main/chart.html',)


def chart2(request):
    print('=================== chart2호출됨.')
    result = []
    with open('static/year_coffee.csv', mode='r') as cafe:
        reader = csv.reader(cafe)

        for list in reader:
            result.append(list)

    print(result)
    return render(request, "main/chart2.html", {'list': result})