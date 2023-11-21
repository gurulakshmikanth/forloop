from django.shortcuts import render

# Create your views here.
def forloops(request):
    d={'name':'kanth'}
    return render(request,'for.html',d)