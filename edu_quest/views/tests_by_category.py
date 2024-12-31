from django.views.generic import ListView

from models_app.models.category.models import Category
from models_app.models.test.models import Test


class ListTestCategoryView(ListView):
    template_name = "tests_by_category.html"
    context_object_name = "tests"

    # Получаем тесты, относящиеся к категории
    def get_queryset(self):
        return Test.objects.filter(category_id=self.kwargs.get("id"), is_published=True)

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст
        context = super().get_context_data(**kwargs)

        # Получаю название категории (для title page)
        category = Category.objects.filter(id=self.kwargs.get("id")).first()

        # Добавляю название категории в контекст
        if category:
            context["category_title"] = category.title

        return context
