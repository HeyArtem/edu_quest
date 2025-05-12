from django.urls import path

from edu_quest.views.favorite_test import toggle_favorite_ajax
from edu_quest.views.home import HomePageView
from edu_quest.views.lerning_ORM import lerning_orm
from edu_quest.views.lerning_ORM_ai import lerning_ORM_ai
from edu_quest.views.question import question_view

# from edu_quest.views.question import RetrieveQuestionView
from edu_quest.views.test import RetrieveTestView
from edu_quest.views.tests_by_category import ListTestCategoryView
from edu_quest.views.user import LoginUserView, LogoutUserView, RegisterUserView
from edu_quest.views.user_result_summary import UserResultSummaryView
from edu_quest.views.user_result_test import user_result_test

# Принцип названия View.
# ActionModelView (Дейсивие Модель View)
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path(
        "categories/<int:id>/",
        ListTestCategoryView.as_view(),
        name="tests_by_category",
    ),
    path("tests/<slug:slug>/", RetrieveTestView.as_view(), name="retrieve_test"),
    path("questions/next/", question_view, name="next_question"),
    path(
        "user_result_summary/", UserResultSummaryView.as_view(), name="user_result_view"
    ),
    path(
        "favorite/<int:test_id>/toggle/", toggle_favorite_ajax, name="toggle_favorite"
    ),
    path("user_result_test/<int:test_id>/", user_result_test, name="user_result"),
    path("lerning_orm/", lerning_orm, name="lerning_orm"),
    path("lerning_ORM_ai/", lerning_ORM_ai, name="lerning_ORM_ai"),
]
