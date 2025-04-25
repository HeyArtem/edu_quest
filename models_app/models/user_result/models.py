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

    # def __str__(self):
    #     return self.date

    def __str__(self):
        return f"Результат пользователя {self.user} по тесту {self.test} от {self.date.strftime('%Y-%m-%d %H:%M:%S')} результаты: {self.answers}"

    def get_progress_percent(self):
        """
        Подсчитывает процент правильных ответов из
        числа данных пользователем ответов.
        """

        # Число вопросов. Получаю из количество ответов так как тест может измениться
        total_questions = self.answers.count()
        if total_questions == 0:
            return 0

        # Количество правильных ответов
        correct_ansers = self.answers.filter(is_correct=True).count()
        progress = (correct_ansers / total_questions) * 100
        return round(progress)

    class Meta:
        db_table = "user_results"
        verbose_name = "Результат прохождения"
        verbose_name_plural = "Результаты прохождения"
