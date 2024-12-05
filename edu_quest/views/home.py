from django.views.generic import TemplateView

from models_app.models.category.models import Category
from models_app.models.test.models import Test


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)

        # Извлекаем категории из базы данных
        categories = Category.objects.all()

        # Извлекаем тестовые карточки из базы данных
        test_cards = Test.objects.filter(is_published=True)

        # Форматируем дату для каждого теста
        for test_card in test_cards:
            test_card.formatted_date = test_card.updated_at.strftime("%Y-%m-%d")

        # Передаём список категорий в шаблон
        context["categories"] = categories
        context["test_cards"] = test_cards
        return context
