from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('hii hlooo hiii')
def second(request):
    return HttpResponse('hello django')