# Django TODO API

This project is a simple TODO List API built with Django Rest Framework.

It allows users to create, view, update and delete TODO tasks.

The API was built as part of a junior developer technical assessment.

## API URL

Live API:

https://todo-api-django-kreq.onrender.com/api/todos/

Home:

https://todo-api-django-kreq.onrender.com/

GitHub Repository

https://github.com/SibusisoSkhosana/todo-api-django.git


## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Docker
- Render (Deployment)
- GitHub (Version Control)
- Postman (API Testing)

## Features

This API can:

- Create a todo
- View all todos
- View one todo
- Update a todo
- Delete a todo

also includes:

- Logging
- Unit tests
- Docker support
- Public deployment
- Input validation (model + serializer level)

## API routes

The following routes are available:

- `GET /api/todos/` - shows all tasks
- `POST /api/todos/` - creates a task
- `GET /api/todos/<id>/` - shows a specific task
- `PUT /api/todos/<id>/` - updates a task
- `DELETE /api/todos/<id>/` - deletes a task

## Run Locally

Clone project:

```bash
git clone https://github.com/SibusisoSkhosana/todo-api-django.git
cd todo-api-django
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash (Windows)
venv\Scripts\activate
```
```bash (Mac and Linux)
source venv\bin\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

## Run Tests

```bash
python manage.py test
```

## Docker

Build container:

```bash
docker-compose up --build
```

## Postman Collection

Postman collection included in this repository.

To use it:

1.Open Postman
2.Click Import
3.Select the .json file from the project root
4.Run requests against the API endpoints

## Notes

This project uses Django best practices with separate:

- models
- serializers
- views
- urls
- tests

The app is deployed publicly and can be tested directly using the provided URL.