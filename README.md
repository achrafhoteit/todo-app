# Django To-Do App with User Authentication


This is a simple Django-based To-Do App that incorporates user authentication. The app allows users to create, update, and manage their to-do tasks in a secure and organized manner. User authentication ensures that each user has a personalized experience with their own tasks.

## Features

- **User Registration and Login:** New users can register with their email and password, and existing users can log in to access their to-do lists.
- **Create Tasks:** Authenticated users can create new tasks with a title and description.
- **Update Tasks:** Users can edit and update their tasks' details as needed.
- **Mark as Completed:** Users can mark tasks as completed, providing a visual indicator of their progress.
- **Delete Tasks:** Users have the option to remove tasks that are no longer needed.
- **User-specific Experience:** Each user's tasks are private and cannot be accessed by other users.


## Installation

1. Clone the repository: 

```
git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app
```

2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Create the database and apply migrations:
```
python manage.py migrate
```
4. Create a superuser account (admin):
```
python manage.py createsuperuser
```
5. Run the development server:
```
python manage.py runserver
```
6. Access the app in your web browser at http://127.0.0.1:8000/.

## Usage

1. Register a new account or log in using your existing credentials.
2. Once logged in, you'll be directed to the main dashboard.
3. Create new tasks by clicking the "Add Task" button and providing a title, deadline date (required), description and category (optional).
4. View and manage your tasks on the dashboard.
5. Edit task details by clicking on the task title.
6. Mark tasks as completed by checking the checkbox inside the edit form.
7. Delete tasks using the "Delete" button associated with each task.
8. Log out from the app when done using the "Log Out" button.

## Project Structure

The project is divided into two apps: task and users. Each app has its own set of templates, views, models, and migrations.

The **task** app handles the management of tasks, including creating, updating, and deleting tasks.
The **users** app manages user authentication and registration.
