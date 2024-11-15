from django.contrib import admin
from django.utils.safestring import mark_safe

from models_app.models import Question


# попробовать картинку
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = (
        "id",
        "text",
        "test",
        "get_html_image",
    )

    # Кликабельность в шапке
    list_display_links = (
        "id",
        "text",
        "test",
        "get_html_image",
    )

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ("text",)

    # Справа Фильтр
    list_filter = (
        "id",
        "text",
        "test",
    )

    # Сортирока порядок
    ordering = (
        "test",
        "id",
        "text",
    )

    # Пагинация
    list_per_page = 3

    # Отображение аватара-картинки
    def get_html_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50>')
        return " - "

    # Подпись в шапке 'Аватар' (не get_html_image )
    get_html_image.short_description = "Картинка"


# Эксперименты
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
