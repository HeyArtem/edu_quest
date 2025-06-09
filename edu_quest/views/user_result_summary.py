from datetime import timedelta

from django.utils import timezone
from django.views.generic import TemplateView

from models_app.models import Favorite, UserResult


class UserResultSummaryView(TemplateView):
    template_name = "user_result_summary.html"

    def get_context_data(self, **kwargs):
        """
        Контекст для сводной страницы с результатами прохождения тестов
        + работа с Избранное
        """
        context = super().get_context_data(**kwargs)

        user = self.request.user
        date_now = timezone.now().date()

        # Подготавливаю данные д\избранного
        user_results = (
            UserResult.objects.filter(user=user)
            .select_related("test")
            .prefetch_related("answers")
            .order_by("-date")
        )

        grouped_results = {}

        for result in user_results:
            # Оставляю только дату (без времени)
            result_date = result.date.date()

            if result_date == date_now:
                group = "Сегодня"

            elif result_date == date_now - timedelta(days=1):
                group = "Вчера"

            else:
                group = result_date.strftime("%d.%m.%y")

            # Создаю словарь с готовыми данными
            annotated_result = {
                "title": result.test.title,
                "num_questions": result.answers.count(),
                "progress": result.get_progress_percent(),
                "date": result.date.strftime("%d.%m.%Y %H:%M"),
                "cover": result.test.cover,
                "test_id": result.test.id,  # добавляем id теста сюда!
                "results_id": result.id,
            }
            print("[!] result.id: ", result.id)

            # Добавляю в нужную группу
            if group not in grouped_results:
                grouped_results[group] = []
            grouped_results[group].append(annotated_result)

        # ❗ Удаляем пустые группы (если они вдруг есть)
        grouped_results = {k: v for k, v in grouped_results.items() if v}

        # Достаю ID тестов, которые в избранном:
        favorite_test_ids = Favorite.objects.filter(user=user).values_list(
            "test_id", flat=True
        )
        context["favorite_test_ids"] = list(favorite_test_ids)
        context["grouped_results"] = grouped_results

        return context
