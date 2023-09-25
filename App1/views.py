from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def vista1(request):
    html="""
    <h1>hola</h1>
    <a href=http://127.0.0.1:8000/vista3>este link conduce para vista 3</a>
    """
    return HttpResponse(html)

def vista3(request):
    html="""
    <h1>hi my name is checkman</h1>
    <a href=http://127.0.0.1:8000/vista1>este link conduce para vista 1</a>
    """
    return HttpResponse(html)