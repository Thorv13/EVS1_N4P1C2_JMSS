from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def vista1(request):
    html="""
    <h1>hola</h1>
    <a href=http://127.0.0.1:8000/vista3>este link conduce para vista 3</a>
    <a href=http://127.0.0.1:8000/vista1>este link conduce para vista 1</a>
    <a href=http://127.0.0.1:8000/vista2>este link conduce para vista 2</a>
    <a href=http://127.0.0.1:8000/vista4>este link conduce para vista 4</a>
    """
    return HttpResponse(html)

def vista3(request):
    html="""
    <h1>hi my name is checkman</h1>
    <a href=http://127.0.0.1:8000/vista1>este link conduce para vista 1</a>
    <a href=http://127.0.0.1:8000/vista2>este link conduce para vista 2</a>
    <a href=http://127.0.0.1:8000/vista3>este link conduce para vista 3</a>
    <a href=http://127.0.0.1:8000/vista3>este link conduce para vista 4</a>
    """
    return HttpResponse(html)