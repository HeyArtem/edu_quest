from django.contrib import admin

from models_app.models import UserResult


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    # Подписи в шапке
    # list_display = ('id', 'test', 'user', 'answers', 'date',)
    list_display = (
        "id",
        "test",
        "user",
        "date",
    )
