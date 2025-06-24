# Django CRUD API Project

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

A full-stack Django project implementing **CRUD (Create, Read, Update, Delete)** operations using Django REST Framework (DRF) and PostgreSQL. Includes an optional HTML frontend interface.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [HTML Frontend (Optional)](#html-frontend-optional)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- RESTful API for CRUD operations
- PostgreSQL database integration (default)
- Django Admin for backend management
- HTML template-based UI for CRUD operations
- CORS support for frontend-backend separation
- Environment-based settings using `.env`

---

## Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap (optional)
- **Tools**: Postman, pgAdmin4

---

## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/django-crud-api.git
    cd django-crud-api
    ```

2. **Create and Activate Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    # If requirements.txt is missing, install manually:
    pip install djangorestframework psycopg2-binary python-decouple
    ```

4. **Configure PostgreSQL Database**

    Create a PostgreSQL database and update the `.env` file:

    ```env
    DB_NAME=your_db_name
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_HOST=localhost
    DB_PORT=5432
    SECRET_KEY=your_django_secret_key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    ```

    Make sure `python-decouple` or `dotenv` is used in `settings.py` to load environment variables.

5. **Run Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create Superuser (for admin access)**

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the Server**

    ```bash
    python manage.py runserver
    ```

    Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## API Endpoints

| Method | Endpoint                   | Description           |
|--------|----------------------------|-----------------------|
| GET    | `/employee/list/`          | List all employees    |
| GET    | `/employee/<id>/`          | Get employee by ID    |
| POST   | `/employee/`               | Create new employee   |
| PUT    | `/employee/<id>/`          | Update employee       |
| DELETE | `/employee/<id>/`          | Delete employee       |

---

## HTML Frontend (Optional)

Navigate to `/employee/list/` to use the basic UI for managing records via forms.

---

## Project Structure

```text
├── EMPLOYEE_PROJECT/
│   ├── LICENSE
│   ├── manage.py
│   ├── README.md
│   ├── requirements.txt
│   ├── .env
│   ├── employee_project/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __pycache__/  # compiled files (hidden)
│   └── employee_register/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│       ├── __pycache__/  # compiled files (hidden)
│       ├── migrations/
│       │   ├── __init__.py
│       │   ├── 0001_initial.py
│       │   ├── 0002_rename_name_employee_full_name.py
│       │   └── __pycache__/  # compiled files (hidden)
│       └── templates/
│           └── employee_register/
│               ├── base.html
│               ├── employee_form.html
│               └── employee_list.html
```

---

## Testing

To run tests, use:

```bash
python manage.py test
```

Add your own tests in `employee_register/tests.py` to ensure code quality and reliability.

---

## Screenshots

Screenshots coming soon! If you have screenshots of the UI or API in action, feel free to contribute.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Sunil Saini**  
[GitHub](https://github.com/Sunil0620)  
[Email](mailto:sunilsaini5652@gmail.com)
