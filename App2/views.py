from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def vista2(request):
    html="""
    <h1>hola que tal x2</h1>
    <a href=http://127.0.0.1:8000/vista4>este link conduce para vista 4</a>
    """
    return HttpResponse(html)


def vista4(request):
    html="""
    <h1>hola sumaniro</h1>
    <a href=http://127.0.0.1:8000/vista2>este link conduce para vista 2</a>
    """
    return HttpResponse(html)


