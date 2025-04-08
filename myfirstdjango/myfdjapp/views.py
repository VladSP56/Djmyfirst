# Create your views here.
#from django.http import HttpResponse

#def data_view(request):
   # return HttpResponse("<h1> This is page of Data</h1><p>Any content can be here.</p>")

#def test_view(request):
   # return HttpResponse("<h1> This is page of Test</h1><p> Another unic content!</p>")
from django.shortcuts import render

def data_view(request):
    return render(request, 'myfdjapp/data.html')

def test_view(request):
    return render(request, 'myfdjapp/test.html')