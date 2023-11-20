from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'ram':'RAMMOHAN'}
    return render(request,'forloop.html',d)