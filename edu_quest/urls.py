from django.urls import path

from edu_quest.views.home import HomePageView
from edu_quest.views.user import RegisterUserView, UserLoginView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
