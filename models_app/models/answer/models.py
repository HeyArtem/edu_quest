from django.db import models


class Answer(models.Model):
    text = models.TextField(verbose_name="Текст")
    is_correct = models.BooleanField(default=False, verbose_name="Является корректным")
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        related_name="answers",
        related_query_name="answer",
        verbose_name="Вопрос",
    )

    def __str__(self):
        return f"{self.text} - {self.is_correct}"

    class Meta:
        db_table = "answers"
        verbose_name = "Ответы варианты"
        verbose_name_plural = "Ответы варианты"
