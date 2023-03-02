# YaMDb

<details>
  <summary>Содержание</summary>
  <ul>
    <li>
      <a href="#описание">Описание</a>
      <ul>
        <li><a href="#-особенности">Особенности</a></li>
        <li><a href="#технологии">Технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#-начало-работы">Начало работы</a>
      <ul>
          <li><a href="#установка">Установка</a></li>
          <li><a href="#запуск-development">Запуск (Development)</a></li>
      </ul>
    </li>
    <li><a href="#-использование">Использование</a></li>
    <li><a href="#-авторы">Авторы</a></li>
  </ul>
</details>

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

<a name="описание"></a>

### 🔥 Особенности

- Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен. Также произведению может быть присвоен жанр.
- Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят оценку.
Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.
- Пользователи могут оставлять комментарии к отзывам.

### Технологии

[![Django][Django-badge]][Django-url]
[![DjangoREST][DjangoREST-badge]][DjangoREST-badge]

## ⚙ Начало Работы

> **Warning**:
> Необходимы предустановленные зависимости:
> - Python 3.7+

### Установка

1. Клонировать репозиторий:

    ```shell
    git clone https://github.com/tvules/YaMDb.git
    cd YaMDb
    ```
    
2. Создать и активировать виртуальное окружение:

    ```shell
    python -m venv venv
    ```
    Для Windows:

    ```shell
    venv\Scripts\activate.bat
    ```

    Для Unix/MacOS:

    ```shell
    source venv/bin/activate
    ```

3. Установить зависимости проекта:

    ```shell
    pip install -r requirements.txt
    ```
    
### Запуск (Development)

1. Выполнить миграции базы данных:

    ```shell
    python manage.py migrate
    ```
    
2. Запустить приложение:

    ```shell
    python manage.py runserver
    ```

## 👀 Использование

[Redoc](https://github.com/tvules/api_yamdb/blob/master/api_yamdb/static/redoc.yaml) — Полная документация к **API** проекта.

> **Note**:
> Для просмотра документации загрузите файл на сайт — https://redocly.github.io/redoc/.

## 🧾 Авторы

- **Андрей Ростовцев** (*Разработчик*) — **[GitHub](https://github.com/Serdron)**
- **Илья Петрухин** (*Тимлид, Разработчик*) — **[GitHub](https://github.com/tvules)**
- **Максим Гребенюк** (*Разработчик*) — **[GitHub](https://github.com/Max-arys)**

<!-- MARKDOWN LINKS & BADGES -->

[Django-url]: https://www.djangoproject.com/

[Django-badge]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white

[DjangoREST-url]: https://www.django-rest-framework.org/

[DjangoREST-badge]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
