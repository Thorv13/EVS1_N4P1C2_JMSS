from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def vista2(request):
    html="""
    <h1>hola que tal x2</h1>
    """
    return HttpResponse(html)


def vista4(request):
    html="""
    <h1>hola sumaniro</h1>
    """
    return HttpResponse(html)


