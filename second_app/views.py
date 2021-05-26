from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App </em>")
    my_dict = {"insert_me": "In the view.py right now"}
    return render(request,'template1/index.html',context=my_dict)

def help(request):
    #return HttpResponse("<b>Help</b> How may I help you?<em></em>")
    my_dict = {"insert_me": "How may I help you?"}
    return render(request,'template1/index.html',context=my_dict)
