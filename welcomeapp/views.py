from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""<html><body><h1>welcome to python world</h1></body></html>""")