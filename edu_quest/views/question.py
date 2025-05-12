import random

from django.shortcuts import redirect, render, reverse

from models_app.models import Question, UserResult
from models_app.models.test.models import Test


def question_view(request):
    user = request.user
    slug_test = request.GET["test_slug"]
    test_db = Test.objects.get(slug=slug_test)  # Получил тест

    user_session_key = f"{user.id}_{slug_test}"
    request.session[f"{user.id}_user_session_key"] = user_session_key  # Для middleware

    # Либо None, либо получили список вопросов,
    session_user_questions = request.session.get(f"{user_session_key}_questions")
    print(f"[!] session_user_questions: {session_user_questions}")

    # # Если в сессии нет списка ответов — создаем его!!! НЕ РАБОТАЕТ
    # if f"{user_session_key}_answers" not in request.session:
    #     request.session[f"{user_session_key}_answers"] = []

    # Если пользователь обновил страницу или просто первый раз зашел на тест
    if request.method == "GET":
        print("[!] произошел GET запрос")

        # Если нет список вопросов
        if not session_user_questions:
            question_ids = list(
                test_db.questions.values_list("id", flat=True)
            )  # Создаю список с id-вопросов
            random.shuffle(question_ids)
            request.session[
                f"{user_session_key}_questions"
            ] = question_ids  # Положил в сессию список с id-вопросов

            if len(question_ids) == len(
                request.session.get(f"{user_session_key}_answers", [])
            ):
                user_result = UserResult.objects.create(user=user, test=test_db)
                user_result.answers.set(request.session[f"{user_session_key}_answers"])
                print("[!] Результат записан", user_result.pk)
                return redirect(reverse("user_result", kwargs={"pk": user_result.pk}))

            request.session[f"{user_session_key}_answers"] = []

            # Записываем в сессию общее кол-во вопросов в тесте (для счетчика)
            request.session[f"{user_session_key}_total"] = len(question_ids)
            session_user_questions = question_ids

        # Если есть список вопросов -> session_user_questions
        question_id = session_user_questions[
            -1
        ]  # Беру из списка id-шников вопросов, последний id
        question_db = Question.objects.get(id=question_id)  # По id получаю вопрос
        total_questions = request.session.get(
            f"{user_session_key}_total"
        )  # Получаю из сессии общее кол-во вопросов в тесте (для счетчика)
        return render(
            request,
            "question.html",
            context={
                "test_slug": slug_test,
                "question": question_db,  # Текущий вопрос
                "answers": question_db.answers.all(),
                "current_question_number": (
                    total_questions - len(session_user_questions) + 1
                ),
                "total_questions": total_questions,
                "category": test_db.category,
            },
        )

    # Если произошел POST запрос (пользователь отвечает на вопрос)
    else:
        answer_id = request.POST["answer_id"]  # получил id ответа
        request.session[f"{user_session_key}_answers"].append(
            answer_id
        )  # id ответа добавил в список ответов
        session_user_questions.pop()  # из списка вопросов забираю вопрос
        request.session[f"{user_session_key}_questions"] = session_user_questions
        return redirect(f"{reverse('next_question')}?test_slug={slug_test}")
