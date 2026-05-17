# DevOps Todo App

A simple Todo web application built with Flask and PostgreSQL, containerized with Docker.

## 🛠️ Tech Stack

- **Backend:** Python, Flask, SQLAlchemy
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose

## 📁 Project Structure
## 🚀 How to Run

**Prerequisites:** Docker Desktop installed and running.

```bash
# Clone the repository
git clone git@github.com:prosenjit72/devops-todo-app.git
cd devops-todo-app

# Run with Docker Compose
docker compose up --build
```

Open browser → `http://localhost:5000`

## ✨ Features

- Add, complete, and delete todos
- Data persisted in PostgreSQL
- Fully containerized with Docker

## 📚 What I Learned

- Writing Dockerfile and understanding layer caching
- Docker Compose for multi-container applications
- Connecting Flask app with PostgreSQL via environment variables
- Container networking — services communicate by name

## 🗺️ Roadmap

- [ ] Phase 2: CI/CD with GitHub Actions
- [ ] Phase 3: Infrastructure as Code with Terraform
- [ ] Phase 4: Kubernetes deployment
- [ ] Phase 5: Monitoring with Prometheus & Grafana