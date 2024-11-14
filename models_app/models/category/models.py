from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
