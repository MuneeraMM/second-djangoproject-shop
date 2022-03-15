from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, welcome to shop products')

def about(request):
    return HttpResponse('this is about page')

def contact(request):
    return HttpResponse('this is contact page')