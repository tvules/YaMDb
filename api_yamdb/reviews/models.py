import datetime as dt

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    """Базовая модель."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s',
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        ordering = ('-pub_date',)


class Category(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'

    def __str__(self):
        return self.title


class Title(models.Model):
    name = models.CharField('Название', max_length=200)
    year = models.IntegerField(
        'Год выпуска', validators=[MaxValueValidator(dt.datetime.now().year)]
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        related_name='titles',
        blank=True,
        verbose_name='Жанр',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='Категория',
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Произведения'
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre.name}-{self.title.name}'


class Review(BaseModel):
    """Модель отзыва."""

    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.TextField('Текст')
    score = models.IntegerField(
        'Оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
    )

    class Meta(BaseModel.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique_review',
            ),
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:30]


class Comment(BaseModel):
    """Модель комментария к отзыву."""

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )
    text = models.TextField('Текст')

    class Meta(BaseModel.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:30]
