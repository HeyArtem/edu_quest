from datetime import timedelta

from django.utils import timezone
from django.views.generic import TemplateView

from models_app.models import UserResult


class UserResultSummaryView(TemplateView):
    template_name = "user_result_summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        date_now = timezone.now().date()

        user_results = (
            UserResult.objects.filter(user=user)
            .select_related("test")
            .prefetch_related("answers")
            .order_by("-date")
        )

        grouped_results = {
            "Сегодня": [],
            "Вчера": [],
        }

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
            }

            # Добавляю в нужную группу
            if group not in grouped_results:
                grouped_results[group] = []
            grouped_results[group].append(annotated_result)

        context["grouped_results"] = grouped_results
        print("grouped_results: ", grouped_results)

        return context
