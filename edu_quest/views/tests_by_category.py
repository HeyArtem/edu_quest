from django.views.generic import ListView

from models_app.models.category.models import Category
from models_app.models.test.models import Test


class TestsByCategoryView(ListView):
    template_name = "tests_by_category.html"
    context_object_name = "test_cards"

    # Получаем тесты, относящиеся к категории
    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return Test.objects.filter(category_id=category_id, is_published=True)

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)

        # Получаю название категории
        category_id = self.kwargs.get("category_id")

        # Получаем объект категории
        category = Category.objects.filter(id=category_id).first()
        # Добавляю название категории в контекст
        context["category_name"] = (
            category.title if category else "Неизвестная категория"
        )

        # Форматируем дату для каждого теста
        test_cards = context["test_cards"]
        for test_card in test_cards:
            test_card.formatted_date = test_card.updated_at.strftime("%Y-%m-%d")

        # # Название категориии
        # context["category_name"] = category.title if category else "Неизвестная категория"
        # context["test_cards"] = test_cards
        return context
