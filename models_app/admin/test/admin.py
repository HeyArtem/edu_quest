from django.contrib import admin

# from models_app.admin.answer.admin import AnswerInline
from models_app.admin.question.admin import QuestionInline
from models_app.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Отображение в теле карточки
    readonly_fields = ("created_at", "updated_at", "id")

    # Подписи в шапке
    list_display = (
        "id",
        "category",
        "title",
        "description",
        "created_at",
        "updated_at",
        "author",
        "is_published",
    )

    # сверху строка навигации по датам
    date_hierarchy = "updated_at"

    # Кликабельность в шапке
    list_display_links = (
        "id",
        "title",
        "category",
        "description",
        "created_at",
        "updated_at",
        "author",
        "is_published",
    )

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = (
        "title",
        "description",
    )

    # Справа Фильтр
    list_filter = (
        "title",
        "category",
        "description",
        "author",
        "created_at",
        "updated_at",
        "is_published",
        "id",
    )

    # Сортирока порядок
    ordering = (
        "category",
        "title",
        "is_published",
    )

    # Пагинация
    list_per_page = 10

    # Эксперименты
    # добавил, что бы в карточке теста выводились вопросы
    # как сделать еще картинки прикрепленные к вопросам???
    inlines = (QuestionInline,)
