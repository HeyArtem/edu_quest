from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from models_app.models.question.models import Question


class RetrieveQuestionView(DetailView):
    model = Question
    template_name = "question.html"
    # context_object_name = "question"
    context_object_name = "coca_cola"

    # Мне нужно отправлять категорию теста

    def get_object(self, queryset=None):
        return get_object_or_404(
            Question, pk=self.kwargs["pk"], test__slug=self.request.GET.get("test_slug")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()

        # Sessions test
        num_visits = self.request.session.get(
            "MY_VARIABLE", 666
        )  # Берем значение или 0 по умолчанию
        test_variable_s = self.request.session.get("TEST_variable_s", "не получилось")
        self.request.session["MY_VARIABLE"] = (
            num_visits + 1
        )  # Увеличиваем счетчик посещений

        # Добавляем категорию теста в контекст
        context["test_category"] = question.test.category
        context["TEST_variable_s"] = test_variable_s
        context["MY_VARIABLE"] = num_visits
        print(num_visits)

        return context
