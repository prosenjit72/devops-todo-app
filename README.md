# DevOps Todo App 🚀

A production-grade DevOps project built with Flask, Docker, Kubernetes, Terraform, and Prometheus+Grafana monitoring.

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python + Flask | Web application |
| PostgreSQL | Database |
| Docker | Containerization |
| Docker Compose | Local multi-container setup |
| GitHub Actions | CI/CD pipeline |
| Docker Hub | Container registry |
| Terraform | Infrastructure as Code (AWS) |
| Kubernetes | Container orchestration |
| Prometheus + Grafana | Monitoring & Alerting |

## 🏗️ Architecture

```
git push
    ↓
GitHub Actions (CI/CD)
    ↓
Docker Build + Test
    ↓
Docker Hub (Image Registry)
    ↓
Terraform (AWS Infrastructure)
    ↓
Kubernetes (Deployment + Auto Scaling)
    ↓
Prometheus + Grafana (Monitoring)
```

## 📁 Project Structure

```
devops-todo-app/
├── app.py                          # Flask application
├── Dockerfile                      # Docker image
├── docker-compose.yml              # Local development
├── requirements.txt                # Python dependencies
├── templates/
│   └── index.html                  # Frontend
├── .github/
│   └── workflows/
│       └── ci.yml                  # CI/CD pipeline
├── terraform/
│   └── main.tf                     # AWS infrastructure
└── kubernetes/
    ├── deployment.yaml             # K8s deployment
    ├── service.yaml                # K8s service
    ├── postgres-secret.yaml        # Database credentials
    ├── postgres-deployment.yaml    # PostgreSQL deployment
    ├── postgres-service.yaml       # PostgreSQL service
    └── grafana-values.yaml         # Monitoring config
```

## 🚀 How to Run

### Local Development
```bash
docker compose up --build
```
Open: `http://localhost:5000`

### Kubernetes (Minikube)
```bash
minikube start
kubectl apply -f kubernetes/postgres-secret.yaml
kubectl apply -f kubernetes/postgres-deployment.yaml
kubectl apply -f kubernetes/postgres-service.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
minikube service todo-app-service --url
```

### AWS Deployment
```bash
cd terraform
terraform init
terraform apply
```

## ✨ Features

- ✅ Todo CRUD operations
- ✅ Containerized with Docker
- ✅ CI/CD with GitHub Actions
- ✅ Auto build and push to Docker Hub
- ✅ AWS infrastructure with Terraform
- ✅ Kubernetes auto-scaling and self-healing
- ✅ PostgreSQL database in Kubernetes
- ✅ Persistent data storage
- ✅ Live monitoring with Prometheus + Grafana

## 📚 What I Learned

- Writing Dockerfile and understanding layer caching
- Docker Compose for multi-container applications
- Building CI/CD pipelines with GitHub Actions
- Infrastructure as Code with Terraform
- Kubernetes deployments, services, and HPA auto-scaling
- PostgreSQL deployment in Kubernetes
- Monitoring with Prometheus and Grafana dashboards

## 🗺️ Roadmap

- [x] Phase 1: Docker + Compose
- [x] Phase 2: CI/CD + Docker Hub
- [x] Phase 3: Terraform + AWS
- [x] Phase 4: Kubernetes
- [x] Phase 5: Monitoring
- [x] Phase 6: PostgreSQL in Kubernetes