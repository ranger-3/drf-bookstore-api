# DRF Bookstore API 📚

A tiny **Django REST Framework** project to manage books and authors.  
Built as a pet-project — just to practice DRF, testing, and Docker.

---

## 🔧 Requirements
- [Docker](https://docs.docker.com/get-docker/)

---

## ✨ What it uses
- [Django REST Framework](https://www.django-rest-framework.org/) (API framework)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/) (OpenAPI schema & docs)
- [pydantic-settings](https://docs.pydantic.dev/latest/usage/pydantic_settings/) (for config)
- [pytest](https://docs.pytest.org/) + [model-bakery](https://model-bakery.readthedocs.io/) (for tests)

---

## 🛠 Dev tools
- [pre-commit](https://pre-commit.com/) (linting & formatting on commit)
- [ruff](https://github.com/astral-sh/ruff) (linter & formatter)

---

## 🚀 How to run

1. Clone the repo and go into the project folder.  

2. Create a `.env` file with your database credentials and secret key:  
   ```bash
   POSTGRES_DB=bookstore
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   SECRET_KEY=your_secret
   DEBUG=True

3. Start the app with Docker Compose:
    ```bash
    docker compose up --build

4. Open the API in your browser:

Swagger UI → http://localhost:8000/api/schema/swagger-ui/
