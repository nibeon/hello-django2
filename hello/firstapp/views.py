from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

# -------
# def index(request):
    # data = {'message': "Hello Gold!"}
    # return render(request, "index.html", context=data)
#    return render(request, "firstapp/home.html")

# -------
def index(request):
    header = "Personal data"
    langs = ["English","German","Spanish"]
    user = {"name": "Tom", "age": 23}
    addr = ("Абрикосовая", 23, 45)

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "bigdatas.html", context=data)


def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")
