# Test-Driven Development with Django 🧪

A Django project built entirely using **Test-Driven Development (TDD)** methodology. The project covers multiple Django concepts — ORM, authentication, blog posts, and a REST API — with every feature written test-first.

---

## What's Inside

This project is structured as multiple learning modules, each demonstrating a different Django feature developed with TDD:

| Module | Description |
|--------|-------------|
| `aa_orm` | Django ORM queries and database interactions |
| `accounts` | User registration, login, and profile management |
| `posts` | Blog post CRUD with views and templates |
| `rest_api` | REST API built with Django REST Framework + JWT |
| `myblog` | Django project settings and configuration |

---

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Django 5 | Web framework |
| Django REST Framework | REST API |
| SimpleJWT | JWT-based authentication |
| PostgreSQL | Production database |
| Redis | Caching + Celery broker |
| Celery + Celery Beat | Async tasks and scheduling |
| coverage | Test coverage reports |
| model-bakery | Test fixture / model factory |
| Faker | Fake data generation for tests |
| Black | Code formatting (PEP 8) |
| django-debug-toolbar | Development debugging |
| django-crispy-forms | Bootstrap 5 form styling |
| libgravatar | Avatar generation from email |
| django-dbbackup | Database backup management |
| GitHub Actions | CI/CD — runs tests on every push |

---

## TDD Workflow

This project follows the **Red → Green → Refactor** cycle:

```
1. 🔴 RED    — Write a failing test for the feature
2. 🟢 GREEN  — Write the minimum code to make it pass
3. 🔵 REFACTOR — Clean up the code without breaking tests
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Redis (optional — for Celery features)

### Installation

```bash
git clone https://github.com/LokRaj-Vuppu/Test-Driven-Developement-using-Django.git
cd Test-Driven-Developement-using-Django

python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

---

## Running Tests

Run all tests:

```bash
python manage.py test
```

Run with coverage report:

```bash
coverage run manage.py test
coverage report
```

Generate an HTML coverage report:

```bash
coverage html
# Open htmlcov/index.html in your browser
```

Run tests for a specific app:

```bash
python manage.py test accounts
python manage.py test posts
python manage.py test rest_api
```

---

## CI/CD

GitHub Actions workflow (`.github/workflows/`) runs tests automatically on every push and pull request using a PostgreSQL service container.

---

## Code Quality

Format code with Black:

```bash
black .
```

---

## Project Structure

```
Test-Driven-Developement-using-Django/
├── .github/workflows/   # GitHub Actions CI
├── aa_orm/              # ORM module + tests
├── accounts/            # User auth module + tests
├── posts/               # Blog posts module + tests
├── rest_api/            # DRF REST API + tests
├── myblog/              # Project settings
├── templates/           # HTML templates
├── static/              # Static assets
├── htmlcov/             # Coverage HTML report
├── manage.py
└── requirements.txt
```

---

## Author

**LokRaj Vuppu** — [GitHub](https://github.com/LokRaj-Vuppu)
