from django import forms


class AuthorisationForm(forms.Form):
    username = forms.CharField(label="ФИО пользователя", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())