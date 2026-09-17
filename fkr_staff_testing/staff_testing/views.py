from django.http import HttpResponse
from django.shortcuts import render

data_db = [
    {'id' : 1, 'title' : 'Опросник 1', 'is_published' : True},
    {'id' : 2, 'title' : 'Опросник 2', 'is_published' : True},
    {'id' : 3, 'title' : 'Опросник 3', 'is_published' : False},
]


def index(request):
    return render(request, 'index.html')


def questionnaire_list(request):
    questionnaires = {
        'questionnaires' : data_db,
    }
    return render(request, 'questionnaire_list.html', context=questionnaires)


def questionnaire(request, id):
    return HttpResponse(f"Страница c опросником {id}")