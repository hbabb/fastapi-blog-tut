# FastAPI Blog Tutorial

A full-stack blogging application built with Python and FastAPI, developed as part of my continued exploration of backend engineering, modern Python development, and application deployment.

This project follows [Corey Schafer's FastAPI tutorial series](https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI), providing hands-on experience building a database-driven web application from initial development through production deployment.

## Project Overview

The application combines an asynchronous REST API with a server-rendered frontend, relational database persistence, user authentication, and cloud-based services.

The primary objective of this project is to gain practical experience with FastAPI and its surrounding ecosystem while exploring the complete lifecycle of a Python web application.

## Features

The project covers the following functionality throughout the tutorial series:

- User registration and account management
- JWT-based authentication and authorization
- Secure password hashing using Argon2
- Blog post creation, retrieval, modification, and deletion
- Asynchronous database operations
- Request and response validation
- Server-rendered HTML templates
- User profile images and file uploads
- Image processing and validation
- Post pagination
- Email-based password recovery
- Cloud object storage
- Database schema migrations
- Automated testing and mocking
- Application health checks
- HTTP security headers
- Containerization and production deployment

## Technology Stack

| Technology | Purpose |
|---|---|
| [Python](https://www.python.org/) | Primary programming language |
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework and REST API |
| [Uvicorn](https://www.uvicorn.org/) | ASGI application server |
| [Pydantic](https://docs.pydantic.dev/) | Data validation and serialization |
| [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Application configuration |
| [SQLAlchemy](https://www.sqlalchemy.org/) | Asynchronous ORM and database access |
| [Alembic](https://alembic.sqlalchemy.org/) | Database migrations |
| [SQLite](https://www.sqlite.org/) | Development database |
| [PostgreSQL](https://www.postgresql.org/) | Production database |
| [Jinja2](https://jinja.palletsprojects.com/) | HTML templating |
| [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | Frontend interactivity |
| [PyJWT](https://pyjwt.readthedocs.io/) | JSON Web Tokens |
| [pwdlib](https://github.com/frankie567/pwdlib) | Password hashing |
| [Pillow](https://python-pillow.org/) | Image processing |
| [Boto3](https://boto3.amazonaws.com/) | AWS service integration |
| [aiosmtplib](https://aiosmtplib.readthedocs.io/) | Asynchronous email delivery |
| [pytest](https://docs.pytest.org/) | Automated testing |
| [Moto](https://docs.getmoto.org/) | AWS service mocking |
| [uv](https://docs.astral.sh/uv/) | Python project and dependency management |
| [Docker](https://www.docker.com/) | Application containerization |

## Getting Started

The following instructions apply to the completed application.

### Prerequisites

- Python 3.12 or newer
- uv
- Git
- PostgreSQL (when using a PostgreSQL database)
- Docker (optional, for containerized deployment)

### Installation

From the root of the repository, install the project dependencies:

```bash
uv sync
```

### Environment Configuration

Create a `.env` file in the project root.

```dotenv
# Database
DATABASE_URL=sqlite+aiosqlite:///./blog.db

# Authentication
SECRET_KEY=replace-with-a-secure-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
RESET_TOKEN_EXPIRE_MINUTES=60

# Object Storage
S3_BUCKET_NAME=your-bucket-name
S3_REGION=us-east-1
S3_ACCESS_KEY_ID=your-access-key
S3_SECRET_ACCESS_KEY=your-secret-access-key

# Application
MAX_UPLOAD_SIZE_BYTES=5242880
POSTS_PER_PAGE=10
FRONTEND_URL=http://localhost:8000

# Email
MAIL_SERVER=localhost
MAIL_PORT=587
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=noreply@example.com
MAIL_USE_TLS=true
```

Generate a secure authentication secret:

```bash
uv run python -c "import secrets; print(secrets.token_hex(32))"
```

For PostgreSQL, replace the database connection string with:

```dotenv
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/fastapi_blog
```

Configure valid object storage and SMTP credentials to enable image uploads and password recovery.

Never commit environment files, credentials, or application secrets to version control.

### Database Migrations

Apply the database migrations:

```bash
uv run alembic upgrade head
```

### Running the Application

Start the development server:

```bash
uv run fastapi dev main.py
```

The application provides the following entry points:

| Endpoint | Description |
|---|---|
| `/` | Blog homepage |
| `/docs` | Interactive Swagger API documentation |
| `/redoc` | ReDoc API documentation |
| `/openapi.json` | OpenAPI specification |
| `/health` | Application and database health check |
| `/api/users` | User API route prefix |
| `/api/posts` | Blog post API route prefix |

The development server is available at http://localhost:8000.

## Testing

The application uses pytest for automated testing and Moto to mock external AWS services.

Run the test suite:

```bash
uv run pytest
```

Run tests with verbose output:

```bash
uv run pytest -v
```

## Docker

The tutorial uses a multi-stage Docker build to package the application and its dependencies while running the production container as a non-root user.

Build the container image:

```bash
docker build -t fastapi-blog .
```

Run the container:

```bash
docker run --rm \
    --env-file .env \
    -p 8080:8080 \
    fastapi-blog
```

The containerized application is available at http://localhost:8080.

When running inside a container, configure the database connection to use a reachable database host. SQLite databases require persistent storage if data must survive container removal.

## Deployment

The tutorial explores two production deployment strategies:

### Virtual Private Server

- Linux server configuration
- PostgreSQL
- Nginx reverse proxy
- SSL/TLS certificates
- Custom domain configuration
- Server security and application management

### Google Cloud Run

- Docker containerization
- Google Cloud Build
- Google Artifact Registry
- Serverless container deployment
- Environment and secret management
- Custom domain configuration

Production deployments require appropriately configured database access, database migrations, object storage, email services, and application secrets.

## Learning Objectives

Through this project, I intend to develop and reinforce my understanding of:

- RESTful API design and implementation
- Asynchronous programming in Python
- Relational database design and management
- Authentication and authorization
- Data validation and serialization
- Application security
- Separation of application concerns
- Automated testing and dependency mocking
- Integration with external services
- Containerization and cloud infrastructure
- Production deployment and application lifecycle management

## Project Status

**In Development**

This repository serves as a personal learning project and practical reference for future FastAPI applications. It will evolve as I progress through the tutorial series, experiment with the underlying technologies, and explore alternative implementation approaches.

## Acknowledgments

Special thanks to **Corey Schafer** for creating the FastAPI tutorial series and making his educational content and accompanying source code available to the developer community.

This repository is my personal implementation of his tutorial project. Credit for the original application, tutorial architecture, and instructional material belongs to Corey Schafer.

If you are interested in learning FastAPI, I highly recommend following his original series and supporting his work.

- [FastAPI Tutorial Series — YouTube](https://www.youtube.com/playlist?list=PL-osiE80TeTsak-c-QsVeg0YYG_0TeyXI)
- [Corey Schafer — YouTube Channel](https://www.youtube.com/@coreyms)
- [Corey Schafer — Patreon](https://www.patreon.com/coreyms)
- [Corey Schafer — GitHub](https://github.com/CoreyMSchafer)
- [Original Project — GitHub](https://github.com/CoreyMSchafer/FastAPI-19-Deployment-Docker-GCR)
- [Corey Schafer — Website](https://coreyms.com/)

This project is independently maintained for educational purposes and is not an official repository associated with Corey Schafer.
