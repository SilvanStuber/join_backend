# Join Backend

## Project Description

Join Backend is a Django Rest Framework (DRF) application designed for task management, contact management, and user authentication. It provides endpoints for creating, updating, and retrieving tasks and user statistics, supporting features like subtasks, priority handling, and detailed task tracking.

---

## Installation

### Prerequisites

- Python 3.10+
- Django 4.x
- Django Rest Framework 3.x

### Steps to Install

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd join_backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. (Optional) Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

The application will now be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Authentication

| Method | Endpoint                      | Description         | Authentication |
| ------ | ----------------------------- | ------------------- | -------------- |
| `POST` | `/api/auth/registration/`     | Register a new user | No             |
| `POST` | `/api/auth/login/`            | Log in a user       | No             |
| `PUT`  | `/api/auth/update-user/<id>/` | Update user details | Yes            |

### Task Management

| Method   | Endpoint                 | Description           | Authentication |
| -------- | ------------------------ | --------------------- | -------------- |
| `GET`    | `/api/board/tasks/`      | List all tasks        | Yes            |
| `POST`   | `/api/board/tasks/`      | Create a new task     | Yes            |
| `GET`    | `/api/board/tasks/<id>/` | Retrieve task details | Yes            |
| `PUT`    | `/api/board/tasks/<id>/` | Update a task         | Yes            |
| `DELETE` | `/api/board/tasks/<id>/` | Delete a task         | Yes            |

### Contacts

| Method   | Endpoint                            | Description            | Authentication |
| -------- | ----------------------------------- | ---------------------- | -------------- |
| `GET`    | `/api/contacts/user_contacts/`      | List all contacts      | Yes            |
| `POST`   | `/api/contacts/user_contacts/`      | Add a new contact      | Yes            |
| `PUT`    | `/api/contacts/user_contacts/<id>/` | Update contact details | Yes            |
| `DELETE` | `/api/contacts/user_contacts/<id>/` | Delete a contact       | Yes            |

### Summary

| Method | Endpoint                | Description            | Authentication |
| ------ | ----------------------- | ---------------------- | -------------- |
| `GET`  | `/api/summary/summary/` | Get a summary of tasks | Yes            |

---

## Database Models

### Task

- **Fields:**
  - `title`: Title of the task
  - `description`: Description of the task
  - `task_status`: Status of the task (`todo`, `done`, etc.)
  - `assigned`: JSON list of assigned users
  - `due_date`: Due date of the task
  - `priority_content`: Priority level of the task
  - `category`: JSON list of categories
  - `creator`: The creator of the task
  - `sub_tasks`: Associated subtasks

### UserContact

- **Fields:**
  - `name`: Name of the contact
  - `email`: Email address of the contact
  - `phone`: Phone number of the contact

### SubTask

- **Fields:**
  - `description`: Description of the subtask
  - `completed`: Completion status

---

## Example Requests

### Creating a Task

**Request:**

```http
POST /api/board/tasks/
Authorization: Bearer <token>
Content-Type: application/json

{
    "title": "Develop new feature",
    "description": "Implement login functionality",
    "task_status": "todo",
    "assigned": ["developer1", "tester1"],
    "due_date": "2024-12-01",
    "priority_content": "priorityUrgent",
    "category": ["Backend", "Auth"],
    "sub_tasks": [
        {"description": "Create API", "completed": false},
        {"description": "Write test cases", "completed": false}
    ]
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Develop new feature",
  "description": "Implement login functionality",
  "task_status": "todo",
  "assigned": ["developer1", "tester1"],
  "due_date": "2024-12-01",
  "priority_content": "priorityUrgent",
  "category": ["Backend", "Auth"],
  "sub_tasks": [
    { "id": 1, "description": "Create API", "completed": false },
    { "id": 2, "description": "Write test cases", "completed": false }
  ]
}
```

---

## Running Tests

To ensure that the project is working as expected, run the following command:

```bash
python manage.py test
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
