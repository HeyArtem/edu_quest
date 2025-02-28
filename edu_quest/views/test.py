from django.views.generic import DetailView

from models_app.models.test.models import Test


class RetrieveTestView(DetailView):
    model = Test
    template_name = "retrieve_test.html"
    context_object_name = "test"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Количество вопросов
        context[
            "question_count"
        ] = self.object.questions.count()  # Добавляем в контекст
        return context
