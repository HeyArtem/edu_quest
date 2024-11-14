from django.contrib import admin

from models_app.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = (
        "id",
        "text",
        "is_correct",
        "question",
    )

    # Кликабельность в шапке
    list_display_links = (
        "id",
        "text",
        "is_correct",
        "question",
    )

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = ("text",)

    # Справа Фильтр
    list_filter = (
        "text",
        "is_correct",
        "question",
        "id",
    )

    # Сортирока порядок
    ordering = (
        "question",
        "is_correct",
        "text",
        "id",
    )

    # Пагинация
    list_per_page = 10


# Эксперименты
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
