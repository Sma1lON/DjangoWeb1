from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    """Категорія"""
    title = models.CharField("Назва", max_length=50)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Тег"""
    title = models.CharField("Тег", max_length=50)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.title


class Blog(models.Model):
    """Стаття"""
    user = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE, default="")
    category = models.ForeignKey(
        Category,
        verbose_name="Категорія",
        on_delete=models.SET_NULL,
        null=True)
    title = models.CharField("Заголовок", max_length=70, default="")
    text_min = models.TextField("Текст", max_length=200, default="")
    text = models.TextField("Текст новини", default="")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField("Дата створення", default=timezone.now)
    description = models.CharField("Опис", max_length=100, default="")
    keywords = models.CharField("Ключові слова", max_length=50, default="")

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статьї"

    def __str__(self):
        return self.title


class Comments(models.Model):
    """Коментарі"""
    user = models.ForeignKey(
        User,
        verbose_name="Користувач",
        on_delete=models.CASCADE)
    new = models.ForeignKey(
        Blog,
        verbose_name="Новина",
        on_delete=models.CASCADE)
    text = models.TextField("Коментар")
    created = models.DateTimeField("Дата добавлення", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерація", default=False)

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

    def __str__(self):
        return "{}".format(self.user)
