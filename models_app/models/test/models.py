import random
import string

from django.db import models
from django.utils.text import slugify


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
    cover = models.ImageField(
        upload_to="users/cover/",
        null=False,  # Разрешает на уровне БД
        blank=False,  # Разрешает при сохранении проекта
        verbose_name="Обложка",
    )

    def generate_unique_slug(self):
        """
        Генерирует уникальный slug:
        сначала пытается без суффикса,
        если уже есть — добавляет случайный суффикс.
        """
        base_slug = slugify(self.title)[:50]  # Ограничиваем длину до 50 символов
        slug = base_slug
        counter = 1

        while Test.objects.filter(slug=slug).exists():
            suffix = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=6)
            )
            slug = f"{base_slug}-{suffix}"
            counter += 1
            # Если за 10 циклов не получилось создать новый slug-break
            if counter > 10:
                break
        return slug

        # Сохранение slug (с предварительной проверкой уникальности)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tests"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
