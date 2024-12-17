from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    """
    Это форма UserCreationForm для регистрации пользователя
    если пароли не совпадут, форма автоматически не пропустит
    """

    username = forms.CharField(
        label="Логин",
        max_length=255,
        widget=forms.TextInput(attrs={"id": "textArea", "class": "login"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            # attrs={'cols': 40, 'rows': 6, 'id': 'textArea', 'class': 'password'}
            attrs={"id": "textArea", "class": "password"}
        ),
    )
    password2 = forms.CharField(
        label="Пароль 2 через CharField звездочки??",
        widget=forms.PasswordInput(attrs={"id": "textArea", "class": "password"})
        # attrs={'cols': 40, 'rows': 6, 'id': 'textArea', 'class': 'password'}
    )

    class Meta:
        """
        Какая модель используется для этой формы
        и какие поля определены для этой формы
        """

        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    """
    Авторизация пользователя
    """

    print("[!]  LoginUserForm from forms.py")
    username = forms.CharField(
        label="Логин",
        max_length=255,
        widget=forms.TextInput(attrs={"id": "textArea", "class": "login"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            # attrs={'cols': 40, 'rows': 6, 'id': 'textArea', 'class': 'password'}
            attrs={"id": "textArea", "class": "password"}
        ),
    )
