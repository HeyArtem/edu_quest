from django.contrib import admin
from django.utils.safestring import mark_safe

from models_app.admin.question.admin import QuestionInline
from models_app.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # Общая страница со всеми тестами - - - - -

    # Подписи в шапке
    list_display = [
        "id",
        "category",
        "title",
        "updated_at",
        "author",
        "is_published",
        "get_html_cover",
        "slug",
    ]

    # сверху строка навигации по датам
    date_hierarchy = "updated_at"

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "title",
        "category",
        "updated_at",
        "author",
        "get_html_cover",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "title",
        "description",
    ]

    # Справа Фильтр
    list_filter = [
        "category",
        "updated_at",
        "is_published",
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
    list_per_page = 30

    # Страница теста содержимое - - - - - - -
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Отображение в теле карточки
    readonly_fields = ["created_at", "updated_at", "id", "get_html_cover"]

    # Блоки в админке
    fieldsets = [
        (
            "Общая информация",
            # {"fields": ["category", "id", "author", "slug"]},
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
                    "cover",
                    "get_html_cover",
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

    # добавил, что бы в карточке теста выводились вопросы
    # как сделать еще картинки прикрепленные к вопросам???
    inlines = (QuestionInline,)

    # Отображение картинки теста (Превью)
    def get_html_cover(self, obj):
        if obj.cover:
            return mark_safe(f'<img src="{obj.cover.url}" height=50 width=50 >')
        return " - "

    # Подпись в шапке 'Аватар' (не get_html_image )
    get_html_cover.short_description = "Превью"


# В разделе "Пользователь" вывожу его "Тесты" (StackedInline-в строку)
class TestInline(admin.StackedInline):
    model = Test
    extra = 0
