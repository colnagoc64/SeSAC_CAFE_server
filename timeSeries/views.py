from django.shortcuts import render

# Create your views here.

def predict(request):
    context = {

    }

    return render(request, 'timeSeries/predict.html', context)