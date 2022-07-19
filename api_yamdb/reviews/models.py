from django.core.validators import MaxValueValidator
from django.db import models
import datetime as dt


class User(models.Model):
    pass


class Categories(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    def __str__(self):
        return self.title


class Genres(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Жанры"
        verbose_name = "Жанр"

    def __str__(self):
        return self.title


class Titles(models.Model):
    name = models.CharField('Название', max_length=200)
    year = models.IntegerField(
        'Год выпуска',
        validators=[MaxValueValidator(dt.datetime.now().year)]
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(
        Genres,
        through='GenresTitles',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Произведения"
        verbose_name = "Произведение"

    def __str__(self):
        return self.name


class GenresTitles(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'
