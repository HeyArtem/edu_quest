from django.urls import path

from edu_quest.views.home import HomePageView
from edu_quest.views.tests_by_category import ListTestCategoryView
from edu_quest.views.user import LoginUserView, RegisterUserView

# Принцип названия View.
# ActionModelView (Дейсивие Модель View)
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path(
        "categories/<int:id>/",
        ListTestCategoryView.as_view(),
        name="tests_by_category",
    ),
]
