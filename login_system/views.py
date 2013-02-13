# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt                                          
from login_system.models import UsersModel
import login_system
from ast import literal_eval

@csrf_exempt
def index(request):
    return render_to_response('index.html', {'response': 'test'})

@csrf_exempt
def add(request):
    postrequest = literal_eval(request.body)
    username = postrequest['user']
    password = postrequest['password']
    errcode = UsersModel.add(username, password)
    if errcode == 1:
        return login(request)
    response = {'errCode':errcode}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

@csrf_exempt
def login(request):
    print 'login!!!'
    postrequest = literal_eval(request.body)
    username = postrequest['user']
    password = postrequest['password']
    errcode = UsersModel.login(username, password)
    response = {'errCode':errcode}
    if errcode>0:
        response = {'errCode':1, 'count':errcode}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

@csrf_exempt
def TESTAPI_resetFixture(request):
    response = {}
    response['errCode'] = UsersModel.TESTAPI_resetFixture()
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

@csrf_exempt
def TESTAPI_unitTests(request):
    response = UsersModel.TESTAPI_unitTests()
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
