from django.shortcuts import render

# Create your views here.


def mlpred(request):

    return render(request, "mlpred/mlpred.html")

def mldate():

    context = {'near_cafe':'hong',
               'field' : 'shoes',
               'email' : 'root@gmail.com',
               'contact' : '010-4444-4444',
               'payValue' :5000
               }
    return render(request,'app1/js11.html',context)