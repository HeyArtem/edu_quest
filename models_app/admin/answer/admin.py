from django.contrib import admin

from models_app.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = [
        "id",
        "text",
        "is_correct",
        "question",
    ]

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "text",
        "is_correct",
        "question",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "text",
        # "question", # Как сделать поиск по тексту вопроса
    ]

    # Справа Фильтр
    list_filter = [
        "is_correct",
    ]

    # Сортирока порядок
    ordering = [
        "question",
        "is_correct",
        "text",
        "id",
    ]

    # Пагинация
    list_per_page = 60


# Инлайн отображение ответов в админка\вопросы
class AnswerInline(admin.TabularInline):
    model = Answer
    # Количество дополнительных пустых ячеек
    extra = 0
