from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('')


def new_products(request):
    return HttpResponse('new products')


