from django.shortcuts import render

from django.http import HttpResponse, HttpRequest




# def index(request: HttpRequest):
#     return HttpResponse("Hello Snake PEPA")


def index(request: HttpRequest):
    # print(dir(request))
    # print(request.GET)
    # print(request.get_full_path())
    # print(request.body)
    # print(request.META)
    return render(request, 'index.html')

