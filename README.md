# ✅ Django Task Manager

A full-featured **To-Do / Task Management Web App** built with Django — featuring **User Authentication**, **CRUD operations**, **task status tracking**, and **deadline management**.

> 🌐 **Live Demo:** *(https://django-tasker-auth.onrender.com/)*
> 📁 **Repository:** [fahadbinsiddique/Django-Task-Manager](https://github.com/fahadbinsiddique/django-tasker-auth)

---

## 📌 About The Project

This project takes Django a step further by implementing a complete task management system with **custom user authentication** (Register/Login/Logout) and full **Create, Read, Update, Delete (CRUD)** operations on tasks. Each task has a title, description, status, and deadline.

---

## ✨ Features

- 🔐 User Registration & Login (Custom AbstractUser)
- 🚪 Logout functionality
- ➕ Add new tasks with title, description, status & deadline
- 📋 View all tasks in a list
- 🔍 View individual task details
- ✏️ Edit / Update existing tasks
- 🗑️ Delete tasks
- 🏷️ Task Status: `Pending` | `InProgress` | `Completed`
- 📅 Deadline tracking with DateField
- 🛠️ Custom Django Admin Panel
- 🎨 Template Inheritance for consistent UI
- 🚀 Deployed on Render with Gunicorn & WhiteNoise

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python 3.12.5 | Backend language |
| Django 6.0.3 | Web framework |
| SQLite | Database |
| Gunicorn | Production WSGI server |
| WhiteNoise | Static file serving |
| HTML & CSS | Frontend |
| Render | Deployment platform |

---

## 📂 Project Structure

```
task_project/
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   ├── master/
│   │   │   ├── base.html
│   │   │   └── nav.html
│   │   ├── home.html
│   │   ├── registration.html
│   │   ├── login.html
│   │   ├── task_list.html
│   │   ├── task_details.html
│   │   ├── add_task.html
│   │   └── edit_task.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── task_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

---

## 🗄️ Models

### UserAuthInfoModel (AbstractUser)
| Field | Type | Description |
|---|---|---|
| full_name | CharField | User's full name |
| username | CharField | Inherited from AbstractUser |
| email | EmailField | Inherited from AbstractUser |
| password | - | Inherited from AbstractUser |

### ToDoModel
| Field | Type | Description |
|---|---|---|
| title | CharField | Task title |
| description | CharField | Task description |
| status | CharField (choices) | Pending / InProgress / Completed |
| deadline | DateField | Task deadline (optional) |

---

## ⚙️ ORM & Auth Operations Used

```python
# User Registration
UserAuthInfoModel.objects.create_user(
    full_name=..., username=..., email=..., password=...
)

# Login / Logout
authenticate(username=username, password=password)
login(request, user)
logout(request)

# Create a task
ToDoModel.objects.create(title=..., status=..., description=..., deadline=...)

# Get all tasks
ToDoModel.objects.all()

# Get single task
ToDoModel.objects.get(id=task_id)

# Filter by status
ToDoModel.objects.filter(status="Completed")

# Update a task
ToDoModel(id=edit_id, title=..., status=..., ...).save()

# Delete a task
ToDoModel.objects.get(id=delete_id).delete()
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.12+ installed
- pip installed

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/fahadbinsiddique/Django-Task-Manager.git

# 2. Navigate to project folder
cd Django-Task-Manager/task_project

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Then open your browser: `http://127.0.0.1:8000`

---

## 🔗 URL Routes

| URL | View | Description |
|---|---|---|
| `/` | home_page | Home — shows Completed tasks |
| `/registration` | regi_page | User Registration |
| `/login/` | login_page | User Login |
| `/logout/` | logout_page | User Logout |
| `/task-list/` | task_list_page | All tasks list |
| `/task-details/<id>/` | task_details_page | Single task details |
| `/add-task/` | add_task_page | Add new task |
| `/edit-task/<id>/` | edit_task | Edit existing task |
| `/delete-task/<id>/` | delete_task | Delete a task |

---



## 🧠 What I Learned

- Custom User Model using `AbstractUser`
- Django Authentication — Register, Login, Logout
- Full CRUD operations with Django ORM
- Status-based filtering of records
- Deadline management with DateField
- Template inheritance for DRY frontend code
- Deploying Django with Gunicorn & WhiteNoise on Render

---

## 🙋‍♂️ Author

**Fahad Bin Siddique**
- GitHub: [@fahadbinsiddique](https://github.com/fahadbinsiddique)
- LinkedIn: *[fahadbinsiddique](https://www.linkedin.com/in/fahadbinsiddique/)*

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
