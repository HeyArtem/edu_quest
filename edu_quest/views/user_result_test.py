from django.shortcuts import get_object_or_404, render

from models_app.models.user_result.models import UserResult


def user_result_test(request, test_id):
    """
    Вывод подробного результата прохождения  конкретного теста
        -должна принимат id-шник записи из UserResult
        -должна проволидировать, что id-user & id кто запросил совподают
        -валидация, что результаты есть в результатах (id=40) ZeroDivisionError: division by zero
    """

    """
    specific_user_result - по id-в таблице результатов получил
    один конкретный результат прохождения (Тест, Пользователь, Дата, Ответы)
    """
    actual_user = request.user
    # Получение результатов прохождения + валидация что id текущего user == id user проходившего тест
    # specific_user_result = get_object_or_404(
    #     UserResult,
    #     id=test_id,
    #     user=actual_user
    # )

    # `select_related`
    specific_user_result = get_object_or_404(
        UserResult.objects.select_related("user"), id=test_id, user=actual_user
    )

    if actual_user == specific_user_result.user:
        """
        Что бы подсчитать прогресс в % нужно
            -Количество вопросов
            -Количество правильных ответов
            -(Количество правильных ответов / Число вопросов) * 100
        """
        # Прогресс в %
        correct_answers = (
            specific_user_result.answers.all().filter(is_correct=True).count()
        )
        total_questions = (
            specific_user_result.answers.all().count()
        )  # Общее количечество ответов (вопросов)

        if total_questions == 0:
            context = {
                "info": "Нет результатов прохождения!",
            }
            return render(request, "plug.html", context)
        if total_questions > 0:
            progress = round((correct_answers / total_questions) * 100)
        else:
            progress = "Нет данных"

        context = {
            "progress": progress,
            "specific_user_result": specific_user_result,
        }
        return render(request, "user_result_test.html", context)

    else:
        # Если запрашиваемый результат принадлежит др пользователю
        context = {
            "info": "За вами не числиться такой результат!",
        }
        return render(request, "plug.html", context)
