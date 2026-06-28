# 🚨 IncidentOps

A production-style Incident Management Platform built using **FastAPI**, **React**, and **SQLModel** that simulates how SRE and Platform Engineering teams manage production incidents.

---

## 📌 Overview

IncidentOps allows engineers to create, track, resolve, and manage incidents through a modern web dashboard.

The application automatically:

- Calculates incident priority
- Assigns owner teams
- Displays live dashboard metrics
- Tracks incident lifecycle
- Provides REST APIs with Swagger documentation

---

# 📷 Dashboard

> Add screenshots here after uploading them.

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Swagger API

![Swagger](screenshots/swagger.png)

---

# ✨ Features

### Incident Management

- Create incidents
- Resolve incidents
- Delete incidents
- View all incidents
- Search incidents

### Automated Business Logic

- Automatic priority assignment (P1–P4)
- Automatic owner team assignment
- Incident status tracking

### Dashboard Analytics

- Total Incidents
- Open Incidents
- Critical Incidents
- Live updates

### REST APIs

- CRUD Operations
- OpenAPI Documentation
- Swagger UI

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn

## Frontend

- React
- Vite
- Axios
- CSS3

## Tools

- Git
- GitHub
- Docker (docker-compose)

---

# 🏗 Architecture

```
                    React + Vite
                          │
                     Axios Requests
                          │
                  FastAPI REST APIs
                          │
                 Business Logic Layer
                          │
             SQLModel ORM + SQLite DB
```

---

# 📂 Project Structure

```
IncidentOps
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── database
│   │   ├── schemas
│   │   ├── services
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# 📡 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/incidents/` | List incidents |
| POST | `/incidents/` | Create incident |
| GET | `/incidents/{id}` | Get incident |
| PUT | `/incidents/{id}` | Update incident |
| DELETE | `/incidents/{id}` | Delete incident |
| PUT | `/incidents/{id}/resolve` | Resolve incident |
| GET | `/dashboard/summary` | Dashboard metrics |

---

# 🚀 Running Locally

## Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 📈 Current Capabilities

- ✅ Incident CRUD
- ✅ Dashboard
- ✅ Search
- ✅ Resolve workflow
- ✅ Delete workflow
- ✅ REST APIs
- ✅ Swagger Documentation
- ✅ Responsive UI

---

# 🔮 Future Enhancements

- User Authentication
- Role Based Access Control
- PostgreSQL
- Redis Cache
- Email & Slack Notifications
- Kubernetes Deployment
- Prometheus Metrics
- Grafana Dashboard
- CI/CD using GitHub Actions
- Docker Images
- Audit Logs

---

# 👩‍💻 Author

**Radha Godavarthi**

Software Engineer | DevOps | Site Reliability Engineering

GitHub:
https://github.com/NagadurgaRadhadevi

---

# 📄 License

MIT License