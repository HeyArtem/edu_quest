from django.views.generic import DetailView

from models_app.models.test.models import Test


class MainTestPage(DetailView):
    model = Test
    template_name = "main_test_page.html"
    context_object_name = "test"
