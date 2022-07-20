from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db.models import Avg
from django.db import models
import datetime as dt


User = get_user_model()


class Category(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Жанры"
        verbose_name = "Жанр"

    def __str__(self):
        return self.title


class Title(models.Model):
    name = models.CharField('Название', max_length=200)
    year = models.IntegerField(
        'Год выпуска',
        validators=[MaxValueValidator(dt.datetime.now().year)]
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles',
        blank=True,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Категория'
    )

    @property
    def rating(self):
        return self.reviews.all().aggregate(Avg('score')).get(
            'score__avg',
            0.00
        )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Произведения"
        verbose_name = "Произведение"

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'
