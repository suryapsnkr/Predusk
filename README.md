# 📚 Book Review API

A simple **Book Review** RESTful API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **Redis** for caching. This project demonstrates clean API design, caching, database migrations, and testing.

---

## 🚀 Features

- ✅ CRUD operations for Books and Reviews
- 🚀 Redis caching for book list endpoint
- 📜 Alembic migrations for schema changes
- 📦 PostgreSQL/SQLite ORM with SQLAlchemy
- 🧪 Unit and integration tests with `pytest`
- 🔍 Swagger UI & ReDoc auto-generated documentation

---

## 📁 Project Structure


---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/book-review-api.git
cd book-review-api

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Option A: PostgreSQL

DATABASE_URL = "postgresql://username:password@localhost:5432/bookdb"

createdb bookdb

Option B: SQLite (for quick testing)

DATABASE_URL = "sqlite:///./bookdb.sqlite3"
