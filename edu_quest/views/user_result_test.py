from django.shortcuts import get_object_or_404, render

from models_app.models.user_result.models import UserResult


def user_result_test(request, pk):
    """
    Вывод подробного результата прохождения  конкретного теста
    """

    user_result = get_object_or_404(
        UserResult.objects.select_related(
            "user",
            "test",
            "test__category",
        ).prefetch_related(
            "answers", "answers__question", "answers__question__answers"
        ),
        id=pk,
        user=request.user,
        # todo Макс если с answers__isnull=False, выходит ошибка
        #  "MultipleObjectsReturned at /user_result_test/63/ get() returned more than one UserResult -- it returned 4!"
        #  и много запросов
        # answers__isnull=False,
    )

    answers = user_result.answers.all()

    if not answers:
        return render(
            request,
            "plug.html",
            {
                "info": "Нет результатов прохождения!",
            },
        )

    correct_answers = answers.filter(is_correct=True).count()
    total_answers = answers.count()

    return render(
        request,
        "user_result_test.html",
        {
            "progress": round((correct_answers / total_answers) * 100),
            "user_result": user_result,
        },
    )
