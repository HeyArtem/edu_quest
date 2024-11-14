from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="tests",
        related_query_name="test",
        verbose_name="Категория",
    )
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    author = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="tests",
        related_query_name="test",
        verbose_name="Автор",
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Слаг")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tests"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
