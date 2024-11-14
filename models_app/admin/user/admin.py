from django.contrib import admin
from django.utils.safestring import mark_safe

from models_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Справа Фильтр
    list_filter = ["is_staff", "date_joined"]
    # Подписи в шапке
    list_display = [
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

    def get_html_avatar(self, obj: User) -> str:
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" height=50 width=50>')
        return " - "

    # Подпись в шапке 'Аватар' (не get_html_image )
    get_html_avatar.short_description = "Аватарка"
