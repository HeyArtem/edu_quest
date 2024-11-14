from django.db import models


class UserResult(models.Model):
    test = models.ForeignKey(
        "Test",
        on_delete=models.CASCADE,
        related_name="user_results",
        related_query_name="user_result",
        verbose_name="Tест",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="user_results",
        related_query_name="user_result",
        verbose_name="Пользователь",
    )
    answers = models.ManyToManyField(
        "Answer",
        related_name="user_results",
        related_query_name="user_result",
        verbose_name="Ответы",
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.date

    class Meta:
        db_table = "user_results"
        verbose_name = "Ответ на вопрос"
        verbose_name_plural = "Ответы на вопросы"
