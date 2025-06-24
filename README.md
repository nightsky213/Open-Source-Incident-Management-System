# 🚨 Incident Management System (Flask + SQLite + Docker + Email)

A beginner-friendly, role-based Incident Management System built using Flask and SQLite — complete with Docker support and optional email notifications.

---

## 🎯 Objective

Build a lightweight incident management portal where:
- Reporters can log issues
- Admins can assign them to engineers
- Engineers can resolve issues
- Everyone has role-based access

---

## 🧰 Tech Stack

| Component   | Technology         |
|------------|--------------------|
| Backend    | Python (Flask)     |
| Database   | SQLite             |
| UI         | HTML + Bootstrap   |
| Auth       | Flask-Login        |
| Email      | Flask-Mail + SMTP  |
| Packaging  | Docker             |
| DevOps     | Git, GitHub        |

---

## 📦 Features

- 🔐 Role-based login (`admin`, `engineer`, `reporter`)
- 📝 Incident reporting and viewing
- 🧑‍🔧 Admin-to-engineer assignment
- ✅ Issue resolution by engineers or admins
- 📧 Optional email alerts (on incident events)
- 🐳 Fully Dockerized for easy deployment

---

## 🚀 Getting Started

### 1. 📁 Clone and Enter the Project

```bash
unzip incident-management-with-docker.zip
cd incident-management
```

---

### 2. 📄 Create `.env` File for Email

In the root folder, create a `.env` file:

```env
EMAIL_USER=youremail@example.com
EMAIL_PASS=your_app_password
```

> ⚠️ Use [App Passwords](https://myaccount.google.com/apppasswords) if using Gmail.

---

### 3. 🐳 Build and Run the App

```bash
docker compose build
docker compose up
```

This will:
- Build the Docker image
- Start Flask on port `5000`

✅ Visit: [http://localhost:5000](http://localhost:5000)

---

### 4. 🧱 Initialize the Database (First Time Only)

Open a new terminal:

```bash
docker ps  # copy container ID or name
docker exec -it <container_id_or_name> bash
```

Now inside container:

```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

---

## 👥 Roles

| Role     | Access                            |
|----------|-----------------------------------|
| Reporter | Create/view own incidents         |
| Engineer | View/resolve assigned incidents   |
| Admin    | Full access: assign, resolve, view|

---

## 🗂 Project Structure

```
incident-management/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
├── config.py
├── run.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 🧪 Sample Workflow

1. Register as `reporter` → Create incident
2. Login as `admin` → Assign to engineer
3. Login as `engineer` → Resolve it

---

## 🔧 Common Commands

| Task                     | Command                   |
|--------------------------|---------------------------|
| Build container          | `docker compose build`     |
| Start container          | `docker compose up`        |
| Stop container           | `docker compose down`      |
| View logs                | `docker compose logs -f`   |
| Access container shell   | `docker exec -it <id> bash`|


---
