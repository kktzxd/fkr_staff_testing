from django.http import HttpResponse
from django.shortcuts import render
from .forms import AuthorisationForm


data_db = [
    {'id' : 1, 'title' : 'Опросник 1', 'is_published' : True},
    {'id' : 2, 'title' : 'Опросник 2', 'is_published' : True},
    {'id' : 3, 'title' : 'Опросник 3', 'is_published' : False},
]


def index(request):
    if request.method == 'POST':
        form = AuthorisationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        return questionnaire_list(request)
    else:
        form = AuthorisationForm()
        return render(request, 'index.html', {'form': form})


def questionnaire_list(request):
    questionnaires = {
        'questionnaires' : data_db,
    }
    return render(request, 'questionnaire_list.html', context=questionnaires)


def questionnaire(request, id):
    return HttpResponse(f"Страница c опросником {id}")