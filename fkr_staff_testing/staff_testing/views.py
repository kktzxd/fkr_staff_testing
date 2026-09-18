from django.http import HttpResponse
from django.shortcuts import render
from .forms import AuthorisationForm
from .check_login import check_login


account_db = [
    {'id' : 1, 'login' : 'person1', 'password' : '1111'},
    {'id' : 2, 'login' : 'person2', 'password' : '2222'},
]
questionnaire_db = [
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
            if check_login(account_db, username, password):
                return questionnaire_list(request)
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = AuthorisationForm()
    return render(request, 'index.html', {'form': form})


def questionnaire_list(request):
    questionnaires = {
        'questionnaires' : questionnaire_db,
    }
    return render(request, 'questionnaire_list.html', context=questionnaires)


def questionnaire(request, id):
    data = {
        'id' : id,
    }
    return render(request, 'questionnaire.html', context=data)