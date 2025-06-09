from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render

from models_app.models.user_result.models import UserResult


def user_result_test(request, pk):
    """
    Вывод подробного результата прохождения  конкретного теста
    """

    user_result = get_object_or_404(
        (
            UserResult.objects.select_related(
                "user",
                "test",
                "test__category",
            )
            .prefetch_related(
                "answers", "answers__question", "answers__question__answers"
            )
            .annotate(
                count_correct_answers=Count(
                    "answers", filter=Q(answers__is_correct=True)
                )
            )
        ),
        id=pk,
        user=request.user,
        answers__isnull=False,
    )

    # answers = user_result.answers.all()
    #
    # correct_answers = answers.filter(is_correct=True).count()
    # total_answers = answers.count()
    print(
        f"user_result.count_correct_answers: {user_result.count_correct_answers}\nuser_result.answers.all().count(): {user_result.answers.all().count()} "
    )
    # todo неправильно считается "user_result.count_correct_answers"
    return render(
        request,
        "user_result_test.html",
        {
            "progress": round(
                (user_result.count_correct_answers / user_result.answers.all().count())
                * 100
            ),
            "user_result": user_result,
        },
    )
