from django.shortcuts import render

from models_app.models import Answer, Question, Test, User, UserResult


def lerning_ORM_ai(request):
    tests_1 = Test.objects.all()
    user_res_1 = UserResult.objects.all()

    # 🔹 ШАГ 2: Простая фильтрация
    tests_2 = Test.objects.filter(is_published=True)

    # 🔹 ШАГ 3: Проход по ForeignKey — __ (двойное подчёркивание)
    # Найти все тесты, созданные пользователем с id=1
    tests_us1_3 = Test.objects.filter(author__id=1)

    # Пример 2: Найти все тесты, у которых автор зовут admin:
    # author__username — это проход через ForeignKey на поле username.
    tests_us_name_3 = Test.objects.filter(author__username="admin")

    # Пример 3: Найти все тесты, у которых категория называется "Математика":
    tests_cat_math_3 = Test.objects.filter(category__title="❖ Математика")

    # Найти все вопросы, у которых тест называется "Russian poetry":
    quest = Question.objects.filter(test__title="Russian poetry")
    print("quest: ", quest)

    # 🔹 ШАГ 4: Обратные связи (related_name)
    # Теперь идём в обратную сторону — от User к Test, от Test к Question.
    # 🔸 Пример 4: Получить все тесты пользователя user:
    user = User.objects.get(id=1)
    tests_us_4 = user.tests.all()  # related_name="tests"

    # 🔸 Пример 5: Получить все вопросы теста:
    test_4 = Test.objects.get(id=1)
    quest_test_4 = test_4.questions.all()  # related_name="questions"

    # 🔹 ШАГ 5: Проход на 2 уровня и более
    # 🔸 Пример 6: Найти все вопросы, у которых тест в категории "Математика"
    quest_cat_math_5 = Question.objects.filter(test__category__title="❖ Математика")

    # 🔸 Пример 7: Найти все ответы, которые принадлежат вопросам из теста "Russian poetry"
    answer_test_5 = Answer.objects.filter(question__test__title="Russian poetry")

    # 🔸 Самостоятельная работа Пример 8: Получить всех пользователей, которые проходили тест с названием "just mathematics".
    # users_just_math_5 = UserResult.objects.filter(test__title="just mathematics")

    users_just_math_5 = User.objects.filter(
        user_result__test__title="just mathematics"
    ).distinct()

    # # ✅ Альтернатива через UserResult:
    # users_just_math_5 = UserResult.objects.filter(test__title="just mathematics").valut_list("user", flat=True).distinct()

    # todo В этом выводе я получаю название теста, пользователя, дату, answer в виде models_app.Answer.None.
    #  А должен был только пользователей и не дублировать
    #  Этот тест проходили два пользователя (User1002 и admin).

    # Длинный вариант, наверное есть короче
    test = UserResult.objects.all()
    all_authors_long_5 = set()
    for i in test:
        if str(i.test) == "just mathematics":
            all_authors_long_5.add(str(i.user))

    # 🔸 Самостоятельная работа Пример 9:
    # Получить все тесты, в которых есть хотя бы один вопрос, содержащий слово "вопр".

    # Здесь я получаю и название теста и текст вопроса, как будто я не дошел до решения пол пути
    # нужно же вывести только тесты, верно? они же не должны дублироваться,
    # мой ответ должен содержать какой-то список, где будут только названия да*?
    # questions_5 = Question.objects.filter(text__contains="вопр")

    questions_5 = (
        Test.objects.filter(question__text__contains="вопр").distinct().order_by("-id")
    )

    # 🔸 Самостоятельная работа  Пример 10: Получить все ответы пользователя с username="admin", которые он дал в тесте "just mathematics".

    # answers_admin = Answer.objects.filter(
    #     user_results__user__username="admin",
    #     user_results__test__title="just mathematics"
    # ).distinct()
    # print(answer_test_5)

    # Это QuerySet
    test_qs = Test.objects.all()
    print(test_qs)
    # <QuerySet [<Test: кузов авто>, <Test: fdnjh>, <Test: frbth>, <Test: dododo>, ...]>
    # К QuerySet я могу применять множесево разных фильтров
    filtered_tests = (
        test_qs.filter(category_id=1).filter(is_published=True).order_by("title")
    )

    # # Это список
    test_qs_list = list(test_qs)
    print(test_qs_list)
    # [<Test: кузов авто>, <Test: fdnjh>, <Test: frbth>, <Test: dododo>, ...]
    # К списку не могу применять фильтры
    filtered_tests_l = []
    for test in test_qs_list:
        if test.category.id == 1:
            filtered_tests_l.append(test)

    return render(
        request,
        "lerning_ORM_ai.html",
        context={
            "tests": tests_1,
            "user_res_1": user_res_1,
            "tests_2": tests_2,
            "tests_us1_3": tests_us1_3,
            "tests_us_name_3": tests_us_name_3,
            "tests_cat_math_3": tests_cat_math_3,
            "tests_us_4": tests_us_4,
            "quest_test_4": quest_test_4,
            "quest_cat_math_5": quest_cat_math_5,
            "answer_test_5": answer_test_5,
            "all_authors_long_5": all_authors_long_5,
            "users_just_math_5": users_just_math_5,
            "questions_5": questions_5,
            "filtered_tests": filtered_tests,
        },
    )
