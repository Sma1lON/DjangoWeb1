from django.db import models
from django.contrib.auth import get_user_model
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


class blog(models.Model):
    """Стаття"""
user = models.ForeignKey(User,verbose_name="Автор",on_delete=models.CASCADE)
category = models.ForeignKey(Category,verbose_name="Категорія",on_delete=models.SET_NULL,null=True)
title = models.CharField("Заголовок", max_length=70)
text_min = models.TextField("Текст", max_length=200)
text = models.TextField("Текст новини")
tags = models.ManyToManyField(Tag, verbose_name="Теги")
created = models.DateTimeField("Дата створення", auto_now_add=True)
description = models.CharField("Опис", max_length=100)
keywords = models.CharField("Ключові слова", max_length=50)

class Meta:
    verbose_name = "Стаття"
    verbose_name_plural = "Статьї"

def __str__(self):
    return self.title

