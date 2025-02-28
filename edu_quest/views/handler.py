from django.views.generic import TemplateView


class Handler404View(TemplateView):
    template_name = "handler404.html"
