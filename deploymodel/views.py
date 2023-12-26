from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home(request):
    return render(request,"home.html")

def result(request):

    cls = joblib.load("finalised_model.sav")

    lis = []
    
    
    lis.append(request.GET.get('R1', 1))
    lis.append(request.GET.get('Na',1))
    lis.append(request.GET.get('Mg',1))
    lis.append(request.GET.get('Al',1))
    lis.append(request.GET.get('Si',1))
    lis.append(request.GET.get('K',1))
    lis.append(request.GET.get('Ca',1))
    lis.append(request.GET.get('Ba',1))
    lis.append(request.GET.get('Fe', 1))
  
    ans = cls.predict([lis])
    return render(request,"result.html",{'ans':ans})