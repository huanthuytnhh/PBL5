# Backend Structure for Smart Home System

## Overview

The backend is built using Django and Django REST Framework (DRF). It is organized into multiple apps to separate concerns and provide modularity. Below is the detailed structure of the backend folder.

## Folder Structure

```
backend/
├── db.sqlite3               # SQLite database file (default for development)
├── manage.py                # Django's command-line utility
├── api/                     # API app for handling RESTful endpoints
│   ├── __init__.py          # Marks the folder as a Python package
│   ├── admin.py             # Admin interface configuration for API models
│   ├── apps.py              # App configuration for the API app
│   ├── models.py            # Models for the API app
│   ├── serializers.py       # DRF serializers for converting models to JSON
│   ├── tests.py             # Unit tests for the API app
│   ├── urls.py              # URL routing for the API app
│   ├── views.py             # Views for handling API requests
│   └── migrations/          # Database migration files for the API app
│       ├── __init__.py      # Marks the folder as a Python package
│       └── ...              # Auto-generated migration files
├── devices/                 # Devices app for managing smart devices
│   ├── __init__.py          # Marks the folder as a Python package
│   ├── admin.py             # Admin interface configuration for Device models
│   ├── apps.py              # App configuration for the Devices app
│   ├── models.py            # Models for the Devices app
│   ├── tests.py             # Unit tests for the Devices app
│   ├── urls.py              # URL routing for the Devices app (if needed)
│   ├── views.py             # Views for handling device-related requests
│   └── migrations/          # Database migration files for the Devices app
│       ├── __init__.py      # Marks the folder as a Python package
│       └── ...              # Auto-generated migration files
├── smart_home/              # Main project folder for global settings
│   ├── __init__.py          # Marks the folder as a Python package
│   ├── asgi.py              # ASGI configuration for asynchronous support
│   ├── settings.py          # Global settings for the Django project
│   ├── urls.py              # Global URL routing for the project
│   ├── wsgi.py              # WSGI configuration for deployment
│   └── __pycache__/         # Compiled Python files (auto-generated)
└── __pycache__/             # Compiled Python files (auto-generated)
```

## Key Components

### 1. **`api/`**

- **Purpose:** Handles RESTful API endpoints for the system.
- **Key Files:**
  - `serializers.py`: Defines how models are converted to/from JSON.
  - `views.py`: Contains logic for handling API requests.
  - `urls.py`: Maps API endpoints to views.

### 2. **`devices/`**

- **Purpose:** Manages smart devices in the system.
- **Key Files:**
  - `models.py`: Defines the `Device` model with fields like `name`, `device_type`, `is_on`, etc.
  - `admin.py`: Configures how devices are displayed in the Django admin interface.

### 3. **`smart_home/`**

- **Purpose:** Contains global settings and configurations for the Django project.
- **Key Files:**
  - `settings.py`: Configures installed apps, middleware, database, etc.
  - `urls.py`: Routes global URLs to app-specific URLs.

## Notes

- **Migrations:** Each app has its own `migrations/` folder for tracking database schema changes.
- **Database:** The default database is SQLite (`db.sqlite3`), but it can be replaced with PostgreSQL or another database for production.
- **Admin Interface:** The admin interface is configured for both `api` and `devices` apps to allow easy management of data.

This structure ensures modularity and scalability, making it easier to maintain and extend the backend as the project grows.
