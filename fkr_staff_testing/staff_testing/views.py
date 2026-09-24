from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import AuthorisationForm
from .check_login import check_login
from .models import Questionnaire


account_db = [
    {'id' : 1, 'login' : 'person1', 'password' : '1111'},
    {'id' : 2, 'login' : 'person2', 'password' : '2222'},
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
    questionnaires = Questionnaire.objects.filter(is_published=True)
    return render(request, 'questionnaire_list.html', {'questionnaires': questionnaires})


def questionnaire(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    data = {
        'questionnaire' : questionnaire.title,
    }
    return render(request, 'questionnaire.html', data)