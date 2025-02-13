# Django CBV DRF TodoApp

A Todo application built using Django, Django REST Framework (DRF), and Class-Based Views (CBV).

## Features

- CRUD operations for managing tasks
- API endpoints using Django REST Framework
- Authentication and permissions
- Optimized with Django Class-Based Views

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL / SQLite (configurable)
- Docker (optional)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/shahramsamar/Django_CBV_DRF_TodoApp.git
   cd Django_CBV_DRF_TodoApp
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Access the app:

   - API: `http://127.0.0.1:8000/api/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## API Endpoints

| Method | Endpoint        | Description               |
|--------|---------------|---------------------------|
| GET    | `/api/todos/`  | List all tasks           |
| POST   | `/api/todos/`  | Create a new task        |
| GET    | `/api/todos/{id}/` | Retrieve a task by ID  |
| PUT    | `/api/todos/{id}/` | Update a task         |
| DELETE | `/api/todos/{id}/` | Delete a task         |

## Docker Support (Optional)

1. Build and run the container:

   ```sh
   docker-compose up --build
   ```

2. The application will be available at `http://127.0.0.1:8000/`.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions, bug fixes, or improvements are welcome!

## License

This project is licensed under the MIT License.

---

**Author:** [Shahram Samar](https://github.com/shahramsamar)
