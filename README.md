# To-Do List REST API

A Dockerized Django REST API for managing personal tasks.

## Features

- User Registration
- JWT Authentication
- CRUD Tasks
- Search
- Pagination
- PostgreSQL
- Docker
- Swagger Documentation
- Unit Tests

---

## Technologies

- Python 3.11
- Django 5
- Django REST Framework
- PostgreSQL
- Docker
- SimpleJWT
- drf-spectacular

---

## Installation

Clone repository

```bash
git clone https://github.com/ReganLema/todo-api.git
```

Enter project

```bash
cd todo-api
```

Copy environment file

```bash
cp .env.example .env
```

Run Docker

```bash
docker compose up --build
```

Apply migrations

```bash
docker compose exec web python manage.py migrate
```

Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

Open Swagger

```
http://localhost:8080/api/docs/
```

Admin

```
http://localhost:8080/admin/
```

---

## API Endpoints

### Authentication

POST

```
/api/accounts/register/
```

POST

```
/api/accounts/login/
```

POST

```
/api/accounts/refresh/
```

---

### Tasks

GET

```
/api/tasks/
```

POST

```
/api/tasks/
```

PUT

```
/api/tasks/{id}/
```

PATCH

```
/api/tasks/{id}/
```

DELETE

```
/api/tasks/{id}/
```

PATCH

```
/api/tasks/{id}/complete/
```

---

## Pagination

```
?page=2
```

---

## Search

```
?search=django
```

---

## Filter

```
?completed=true
```

---

## Ordering

```
?ordering=-created_at
```

---

## Documentation

Swagger

```
http://localhost:8080/api/docs/
```

---

## Author

Regan Simon Lema

GitHub

https://github.com/ReganLema/todo-api