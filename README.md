FASTAPI HTML User Registration App

This project is a simple and clean User Registration Web Application built using FastAPI, SQLModel, Jinja2 Templates, and SQLite.
Users can register with their name, email, and phone number, and all submitted records are stored in the database and displayed in a users table.

Features
-> User registration form (HTML frontend with CSS styling)

-> Stores user details in SQLite database

-> Displays all registered users in a clean table

-> FastAPI backend with SQLModel ORM

-> Templating with Jinja2

->  Modular project structure with routes and database management

Project Structure

FASTAPI_HTML/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── user_routes.py
│   ├── templates/
│   │     ├── register.html
│   │     ├── users.html
│   └── static/
│         └── style.css
│
├── requirements.txt
└── README.md

Tech Stack

| Component         | Technology Used |
| ----------------- | --------------- |
| Backend Framework | FastAPI         |
| ORM               | SQLModel        |
| Database          | SQLite          |
| Templates         | Jinja2          |
| Styling           | CSS             |
| Server            | Uvicorn         |


How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start the FastAPI server
uvicorn app.main:app --reload

3️⃣ Open in Browser

->  Registration Page:
http://127.0.0.1:8000/

-> Users List Page:
http://127.0.0.1:8000/users

🗄️ Database
-> The project uses a simple SQLite database: users.db
-> Tables are automatically created using:- SQLModel.metadata.create_all(engine)

