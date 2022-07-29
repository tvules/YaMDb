# api_yamdb
### Описание
Api_yamdb — это сервис о музыке, фильмах и книгах. На нем вы сможете узнать рейтинги популярных произведений поставить им оценки, написать рецензии и комментарии к ним.
### Технологии
- Python 3.7
- Django==2.2.16
- djangorestframework==3.12.4
### Запуск проекта в dev-режиме
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов
- Используется аутентификация с использованием JWT-токенов
- Header parameter name: Bearer

- Регистрация:
При валидных данных на указанную почту будет выслан секретный код для получения токена.
POST http://127.0.0.1:8000/api/v1/auth/signup/

```json
{
    "email": "string",
    "username": "string"
}
response
{
    "email": "string",
    "username": "string"
}
```
- Получение стокена:
POST http://127.0.0.1:8000/api/v1/auth/token/
```json
{
    "username": "string",
    "confirmation_code": "string"
}
response
{
  "token": "string"
}
```
- Получение списка всех категорий:
GET http://127.0.0.1:8000/api/v1/categories/

```json
response
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results":
      [...]
  }
]
```
- Получение списка всех жанров:
GET http://127.0.0.1:8000/api/v1/genres/

```json
response
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results":
      [...]
  }
]
```
- Получение списка всех произведений:
GET http://127.0.0.1:8000/api/v1/titles/

```json
response
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results":
      [...]
  }
]
```
- Добавление произведения:
POST http://127.0.0.1:8000/api/v1/titles/

```json
{
    "name": "string",
    "year": 0,
    "description": "string",
    "genre": ["string"],
    "category": "string"
}
response
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre":
    [{...}],
  "category": 
    {
      "name": "string",
      "slug": "string"
    }
}
```
- Получение информации о произведении:
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/

```json
response
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": 
    [{...}],
  "category": 
    {
      "name": "string",
      "slug": "string"
    }
}
```
- Получение списка всех отзывов:
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

```json
response
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": 
      [...]
  }
]
```
- Добавление нового отзыва:
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/

```json
{
  "text": "string",
  "score": 1
}
response
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- Полуение отзыва по id:
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

```json
response
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- Редактирование отзыва по id:
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

```json
{
  "text": "string",
  "score": 1
}
response
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- Удаление отзыва по id:
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/

- Получение списка всех комментариев к отзыву:
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

```json
response
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": 
      []
  }
]
```
- Добавление комментария к отзыву:
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/

```json
{
  "text": "string"
}
response
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- Получение комментария к отзыву:
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```json
response
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- Pедактирование комментария к отзыву:
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

```json
{
  "text": "string"
}
response
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- Удаление комментария к отзыву:
DELETE http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

- Получение данных своей учетной записи:
GET http://127.0.0.1:8000/api/v1/users/me/

```json
{
  "text": "string"
}
response
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
- Изменение данных своей учетной записи:
PATCH http://127.0.0.1:8000/api/v1/users/me/

```json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
response
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
### Авторы
- [Андрей Ростовцев](https://github.com/Serdron)
- [Илья Петрухин](https://github.com/tvules)
- [Максим Гребенюк](https://github.com/Max-arys)
