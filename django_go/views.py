from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django_go.models import Asset, UserInfo
from django_go.form import registerForm


# from django_go.
# Create your views here.

def index(request):
	return HttpResponse('i111122213313')


def list1(request, name, id):
	print name, id
	return HttpResponse('list1111111')


def Add(request, name):
	Asset.objects.create(host=name)

	return HttpResponse('ok')


def Delete(request, name):
	'''
	filter
	:param request:
	:param name:
	:return:
	'''

	Asset.objects.filter(host=name).delete()

	return HttpResponse('ok')


def AssetList(request):
	asset_list = Asset.objects.all()

	return render_to_response('assetlist.html', {'data': asset_list, 'user': 'lzj'})


def Login(request):
	if request.method == 'GET':
		return render_to_response('login.html')
	else:
		user = request.POST.get('username', None)
		passwd = request.POST.get('password', None)
		# print user, passwd
		user_check = UserInfo.objects.filter(username=user, password=passwd).count()
		if user_check == 1:
			return HttpResponse('ok')
		else:
			return render_to_response('login.html', {'status': 'denglucuowu'})


def register(request):
	registerform = registerForm()

	if request.method == 'POST':
		form1 = registerForm(request.POST)
		if form1.is_valid():
			data = form1.clean()
			print data['username']
			UserInfo.objects.create(username=data['username'], password=data['email'])
		else:
			print form1.errors
			return render_to_response('register.html', {'form': registerform})
	return render_to_response('register.html', {'form': registerform})
