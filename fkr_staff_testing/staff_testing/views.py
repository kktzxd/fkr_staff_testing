from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения staff_testing")


def authentification(request):
    return HttpResponse("Страница аутентификации")


def questionnaire_list(request):
    return HttpResponse("Страница со списком опросников")


def questionnaire(request, id):
    return HttpResponse(f"Страница c опросником {id}")