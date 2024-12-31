from django.views.generic import TemplateView

from models_app.models.category.models import Category
from models_app.models.test.models import Test


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)

        # Передаём список категорий в шаблон
        # Извлекаем категории из базы данных
        context["categories"] = Category.objects.all()
        # Извлекаем тестовые карточки из базы данных
        context["tests"] = Test.objects.filter(is_published=True)[
            :6
        ]  # Берём только первые 6 карточек
        return context
