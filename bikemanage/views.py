# -*- coding:utf-8 -*-
import json

from django.core import serializers
from django.forms import model_to_dict

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from . import models
from models import User, Bike, Recoder
# Create your views here.

@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User(user_id=request.GET.get('userId'), user_name=request.GET.get('userName'), password=request.GET.get('password'),
                    telephone=request.GET.get('telephone'), qq_number=request.GET.get('qqNumber'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = e.message
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def add_bike(request):
    response = {}
    try:
        user = models.User.objects.get(user_id = request.GET.get('userId'))
        bike = Bike(bike_id = request.GET.get('bikeId'), monster = user, status = request.GET.get('status'),
                    longitude=request.GET.get('longitude'), latitude=request.GET.get("latitude"))
        bike.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = e.message
        response['error_num'] = 1
    return JsonResponse(response)



@require_http_methods(["GET"])
def show_user(request):
    response = {}
    try:
        userId = request.GET.get('userId')
        response['user'] = model_to_dict(models.User.objects.get(user_id = userId))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = e.message
        response['error_num'] = 1

    return JsonResponse(response, json_dumps_params={'ensure_ascii':False})



@require_http_methods(["GET"])
def show_bike(request):
    response = {}
    try:
        userId = request.GET.get('userId')
        response['bike'] = model_to_dict(Bike.objects.get(monster_id =userId))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = e.message
        response['error_num'] = 1

    return JsonResponse(response,json_dumps_params={'ensure_ascii':False})


@require_http_methods(["GET"])
def show_bikes(request):
    response = {}
    try:
        userId = request.GET.get('userId')
        bikes = Bike.objects.filter(monster_id =userId)
        response['bikes'] = serializers.serialize('json', bikes)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception,e:
        response['msg'] = e.message
        response['error_num'] = 1

    return JsonResponse(response,json_dumps_params={'ensure_ascii':False})


# status:
# 0 locked
# 1 unlocked
# 2 loss
@require_http_methods(["GET"])
def update_bike_status(request):
    response = {}
    try:
        bike = Bike.objects.get(bike_id=request.GET.get('bikeId'))
        recorder = Recoder(bike=bike, status=request.GET.get('status'), longitude=request.GET.get('longitude'),
                           latitude=request.GET.get('latitude'))
        recorder.save()
        bike.status = request.GET.get('status')
        bike.longitude = request.GET.get('longitude')
        bike.latitude = request.GET.get('latitude')
        bike.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception, e:
        response['msg'] = e.message
        response['error_num'] = 1
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def update_user(request):
    response = {}
    try:
        user = User.objects.get(user_id=request.GET.get('userId'))
        user.user_name = request.GET.get('userName')
        user.telephone = request.GET.get('telephone')
        user.qq_number = request.GET.get('qqNumber')
        user.password = request.GET.get('password')
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception, e:
        response['msg'] = e.message
        response['error_num'] = 1

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})



