from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def vista1(request):
    html="""
    <h1>say your name</h1>
    """
    return HttpResponse(html)


def vista3(request):
    html="""
    <h1>hi my name is checkman</h1>
    """
    return HttpResponse(html)


