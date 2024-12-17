from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from edu_quest.forms import LoginUserForm, RegisterUserForm


class RegisterUserView(CreateView):
    # Какая форма исп-ся для реги-ции
    form_class = RegisterUserForm

    # Шаблон котор будет исполь-ся
    template_name = "register.html"

    # Когда пользователь ввел свои данные
    def form_valid(self, form):
        # Сохраняю пользователя
        user = form.save()

        # Логиню пользователя
        login(self.request, user)
        return redirect("home")


class UserLoginView(LoginView):
    """
    Авторизация пользователя
    """

    print("[!]  UserLoginView from user.py")
    # Форма для логина
    form_class = LoginUserForm
    template_name = "login.html"
    print("[!] form_class:", form_class)

    # В случае успеха
    def get_success_url(self):
        return reverse_lazy("home")
