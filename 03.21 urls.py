import random

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import path, reverse

from edu_quest.views.home import HomePageView
from edu_quest.views.tests_by_category import ListTestCategoryView
from edu_quest.views.user import LoginUserView, RegisterUserView
from models_app.models import Question, Test, UserResult


def test_view(request):
    test = Test.objects.get(id=1)
    return render(request, "test_html.html", context={"test": test})


def question_view(request):
    user = request.user

    # slug теста, который сейчас проходит пользователь
    slug_test = request.GET["test_slug"]

    # получаем тест из БД по слагу, с которым будем работать
    test_db = Test.objects.get(slug=slug_test)

    # Формируем уникальную-строку (префикс) для работы с сессией пользователя
    user_session_key = f"{user.id}_{slug_test}"

    request.session[f"{user.id}_user_session_key"] = user_session_key

    # Пытаемся из сессии получить список вопросов для пользователя
    # или получим None, если пользователь только зашел на тест
    session_user_questions = request.session.get(
        f"{user_session_key}_questions"
    )  # [3, 2, 1, 5] or None

    # Если пользователь обновил страницу или просто первый раз зашел на тест
    if request.method == "GET":
        # Если у пользователя еще нет вопросов для теста
        if not session_user_questions:
            # Создаем список с айди вопросами из БД с помощью related_name
            question_ids = list(test_db.questions.values_list("id", flat=True))
            # Перемешиваем сформированный список айдишников
            random.shuffle(question_ids)
            # Записываем в сессию список айдишников вопросов
            request.session[f"{user_session_key}_questions"] = question_ids

            # Если длина списка айди == длине ответов, которые дал пользователь
            if len(question_ids) == len(
                request.session.get(f"{user_session_key}_answers", [])
            ):
                # Создали запись, что пользователь завершил тест и мы фиксируем его ответы
                user_result = UserResult.objects.create(user=user, test=test_db)
                # Обратились к результатам пользователя -> поле answers
                # -> записали туда список айдишников ответов пользователя
                user_result.answers.set(request.session[f"{user_session_key}_answers"])
                return redirect(
                    reverse("user_result_view", kwargs={"pk": user_result.pk})
                )

            # Записываем в сессию пустой список с ответами для пользователя.
            # 1. Если пользователь только начал проходить тест, то подготавливаем переменную в сессии
            # 2. Если пользователь полностью прошел тест, то мы зануляем его ответы
            request.session[f"{user_session_key}_answers"] = []

            # Записываем в сессию общее кол-во вопросов в тесте
            request.session[f"{user_session_key}_total"] = len(question_ids)
            # Записываем в переменную список айдишников с вопросами
            session_user_questions = question_ids

        # Получаем последний айдишник из списка вопросов
        question_id = session_user_questions[-1]
        # Получаем вопрос из БД по айдишнику вопроса, который получили выше
        question_db = Question.objects.get(id=question_id)
        # Получили из сессии общее кол-во вопросов в тесте
        # (в сессию мы это записали в момент, когда пользователь только зашел на страницу с тестом)
        total_questions = request.session.get(f"{user_session_key}_total")
        return render(
            request,
            "question_html.html",
            {
                "test_slug": slug_test,
                "question": question_db,
                "answers": question_db.answers.all(),
                "current_question_number": (
                    total_questions - len(session_user_questions)
                )
                + 1,
                "total_questions": total_questions,
            },
        )
    else:  # Если произошел POST запрос (пользователь отвечает на вопрос)
        # Получаем из словаря POST айди ответа, на который нажал пользователь
        answer_id = request.POST["answer_id"]
        # Обращаемся к сессии (список ответов) добавляем ответ пользователя (айди ответа)
        request.session[f"{user_session_key}_answers"].append(answer_id)
        # Из списка вопросов удаляем последний элемент (вопрос)
        session_user_questions.pop()
        # Перезаписываем список вопросов для пользователя, но уже с одним удаленным вопросом
        request.session[f"{user_session_key}_questions"] = session_user_questions
        # Перенаправляем пользователя с помощью redirect
        # reverse - формирует url маршрут основываясь на названиии маршрута. Возвращает строку.
        # Приписываем ?test_slug={slug_test},
        # чтобы при GET запросе у нас сохранился тест пользователя, который он проходит
        return redirect(f"{reverse('next_question')}?test_slug={slug_test}")


def user_result_view(request, pk: int):
    try:
        user_result = UserResult.objects.get(pk=pk, user=request.user)
    except UserResult.DoesNotExist:
        return redirect("home")
    return render(request, "user_result.html", context={"user_result": user_result})


urlpatterns = [
    path("", test_view, name="home"),
    path("questions/next/", question_view, name="next_question"),
    path("user_results/<int:pk>/", user_result_view, name="user_result_view"),
    path("", HomePageView.as_view(), name="home"),
    # ActionModelView.as_view()
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path(
        "categories/<int:id>/",
        ListTestCategoryView.as_view(),
        name="tests_by_category",
    ),
]
