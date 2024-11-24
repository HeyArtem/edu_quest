from django.contrib import admin
from django.utils.safestring import mark_safe

from models_app.admin.test.admin import TestInline
from models_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Кнопка сохранить еще и сверху
    save_on_top = True

    # Подписи в шапке
    list_display = [
        "id",
        "username",
        "is_staff",
        "is_active",
        "date_joined",
        "get_html_avatar",
    ]

    # Кликабельность в шапке
    list_display_links = [
        "id",
        "username",
        "is_staff",
        "is_active",
        "date_joined",
        "get_html_avatar",
    ]

    # По каким полям можно осущ-ять поиск (только CharField или TextField)
    search_fields = [
        "username",
    ]

    # Справа Фильтр
    list_filter = ["is_staff", "is_active", "date_joined"]

    # Сортирока порядок
    ordering = [
        "is_staff",
        "date_joined",
        "is_active",
    ]

    # Пагинация
    list_per_page = 10

    # сверху строка навигации по датам
    date_hierarchy = "date_joined"

    # Вывод тестов пользователя в карточке
    inlines = [
        TestInline,
    ]

    # Поля, котор будут отображаться в форме (работает вкупе с readonly_fields)
    fields = [
        "id",  # (работает вкупе с readonly_fields)
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "password",
        "is_staff",
        "date_joined",
        "last_login",
        "get_html_avatar",  # (работает вкупе с readonly_fields)
        "is_superuser",
        "groups",
        "user_permissions",
    ]

    # Поля в форме только для чтения
    readonly_fields = [
        "id",
        "get_html_avatar",
    ]

    # Отображение аватара в разделе Пользователи
    def get_html_avatar(self, obj: User) -> str:
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" height=50 width=50>')
        return " - "

    # Подпись в шапке 'Аватар' (не get_html_image )
    get_html_avatar.short_description = "Аватарка"
