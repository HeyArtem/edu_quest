from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="favorites",
        related_query_name="favorite",
        verbose_name="Пользователь",
    )
    test = models.ForeignKey(
        "Test",
        on_delete=models.CASCADE,
        related_name="favorites",
        related_query_name="favorite",
        verbose_name="Тест",
    )

    def __str__(self):
        return f"{self.test_id} - {self.user_id} - {self.user.username} ❤️ {self.test.title}"

    class Meta:
        db_table = "favorites"
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        unique_together = ("user", "test")  # чтобы не было дубликатов
