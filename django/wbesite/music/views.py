from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> This music app </h1>")


def song(request):
    return HttpResponse("<h1>songs list</h1>")
