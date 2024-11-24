from django.contrib import admin

from models_app.admin.question.admin import QuestionInline
from models_app.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = [
        "id",
        "category",
        "title",
        "description",
        "updated_at",
        "author",
        "is_published",
    ]

    # сверху строка навигации по датам
    date_hierarchy = "updated_at"

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "title",
        "category",
        "description",
        "updated_at",
        "author",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "title",
        "description",
    ]

    # Справа Фильтр
    list_filter = [
        "title",
        "category",
        "author",
        "updated_at",
        "is_published",
        "description",
        "created_at",
    ]

    # Возможность отредачить мышкой (is_published/is NOT )
    list_editable = ("is_published",)

    # Сортирока порядок
    ordering = [
        "category",
        "title",
        "is_published",
    ]

    # Пагинация
    list_per_page = 10

    # Отображение в теле карточки
    readonly_fields = ["created_at", "updated_at", "id"]

    # добавил, что бы в карточке теста выводились вопросы
    # как сделать еще картинки прикрепленные к вопросам???
    inlines = (QuestionInline,)

    # Блоки в админке
    fieldsets = [
        (
            "Общая информация",
            {
                "fields": [
                    "category",
                    "id",
                    "author",
                ]
            },
        ),
        (
            "Информация о тесте",
            {
                "fields": [
                    "title",
                    "description",
                    "is_published",
                ]
            },
        ),
        (
            "Прочая информация",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    ]


# В разделе "Пользователь" вывожу его "Тесты"
class TestInline(admin.TabularInline):
    model = Test
    extra = 0
