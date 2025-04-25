import datetime

from django.db.models import Q
from django.shortcuts import render

from models_app.models import Answer, Test, User, UserResult


def lerning_orm(request):
    # Вывести первые 5 тестов в бд. Отсортировать по заголовку (в алфавитном порядке)
    test_res_1 = Test.objects.all().order_by("title")[:5]

    # Достать один любой тест из БД. Вывести список всех его вопросов (Только текст).
    # Обращаться к таблице Question - нельзя
    random_test = Test.objects.get(id=1)
    questions_2 = random_test.questions.all()

    # Вывести все правильные ответы от любого теста в БД
    answers_3 = Answer.objects.filter(
        is_correct=True,
        # question__test_id=1
        question__test=random_test,
    )

    # Вывести все не опубликованные тесты из БД
    # not_published_tests_4 = Test.objects.filter(is_published=False)
    not_published_tests_4 = Test.objects.exclude(is_published=True)

    # Вывести тесты, у которых id есть в списке [1, 24, 14, 27]
    list_tests_5 = Test.objects.filter(id__in=[1, 24, 14, 27, 777])

    # # todo AI не может я и подавно!
    # # Вывести все результаты тестов текущего пользователя. Обращаться к таблице UserResult - нельзя
    user = User.objects.get(id=1)
    resault_user_6 = user.user_results.all().order_by("date")

    # примитивный вар
    resault_user_6_2 = UserResult.objects.filter(user_id=user.id)

    # Вывести все результаты тестов текущего пользователя и отфильтровать их по текущей дате.
    # Обращаться к таблице UserResult - нельзя
    user = User.objects.get(id=1)
    resault_user_7 = user.user_results.all().filter(
        date__date=datetime.datetime.now().date()
    )
    print("resault_user_7: ", resault_user_7)

    # Вывести тесты, у которых название начина-ся на м
    list_tests_8 = Test.objects.filter(title__istartswith="м")

    # Вывести тесты, у которых название начина-ся на м или т
    res_tests_m_t_9 = Test.objects.filter(
        Q(title__startswith="м") | Q(title__startswith="т")
    )

    return render(
        request,
        "lerning_ORM.html",
        context={
            "test_res_1": test_res_1,
            "questions_2": questions_2,
            "answers_3": answers_3,
            "not_published_tests_4": not_published_tests_4,
            "list_tests_5": list_tests_5,
            "resault_user_6": resault_user_6,
            "resault_user_7": resault_user_7,
            "list_tests_8": list_tests_8,
            "res_tests_m_t_9": res_tests_m_t_9,
            "resault_user_6_2": resault_user_6_2,
            # "resault_user_6": resault_user_6,
        },
    )
