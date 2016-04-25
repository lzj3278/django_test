from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.


def index(request):
	return HttpResponse('app11111')


def list1(request, name, id):
	print name, id
	return HttpResponse('aaa1111ppp')
