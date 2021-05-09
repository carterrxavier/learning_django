from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1> Hi its xavier </h1>")


def v1(response):
    return HttpResponse("<h1> This is page number 2!</h1>")