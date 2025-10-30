# 📚 Books Catalog API — Capstone Project
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Framework](https://img.shields.io/badge/Framework-Django%20REST%20Framework-green)
![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Build](https://img.shields.io/badge/Build-Docker%20%7C%20Helm%20%7C%20ArgoCD-purple)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A **Django REST API** built as part of my **DevOps Diploma 2025**.  
This project demonstrates my full DevOps workflow — from **local Docker development** to **automated CI/CD and GitOps deployment** on Kubernetes using **Helm**, **GitHub Actions**, and **Argo CD**.

---

## ✨ Features
- CRUD operations for managing books (Add, View, Edit, Delete)  
- REST API endpoints with input validation  
- PostgreSQL database integration  
- Containerized using **Docker** and **docker-compose**  
- CI/CD pipeline with **GitHub Actions** → **GHCR** → **Kubernetes (Helm)**  
- Automated GitOps sync using **Argo CD**  

🎥 **Demo Video:** [Watch Here](https://drive.google.com/file/d/1NxA__cKcy-rY1JbEnpt1PRFRszDmJ6wI/view?usp=sharing)

---

## 🧩 Tech Stack

| Tool | Purpose |
|------|----------|
| **Python 3.12** | Backend programming |
| **Django REST Framework** | API framework |
| **PostgreSQL** | Relational database |
| **Docker / Docker Compose** | Containerization |
| **Helm** | Kubernetes deployment |
| **Argo CD** | GitOps automation |
| **GitHub Actions** | CI/CD automation |
| **GHCR (GitHub Container Registry)** | Image hosting |

---

## 1. Project Overview
- **Framework:** Django REST Framework  
- **Database:** PostgreSQL  
- **Deployment:** Helm on Kubernetes  
- **CI/CD:** GitHub Actions → GHCR → K8s  
- **Main Features:**
  - Title, Author, ISBN, Published Date, Status
  - Full CRUD API with validation

---

## 2. API Usage Examples

Base URL in local development: `http://127.0.0.1:8000/api/books/` or  `http://localhost:8000/api/books/`
Base URL in Kubernetes (Ingress): `http://localhost:8081/api/books/`

**List all books**
```bash
curl http://127.0.0.1:8000/api/books/ | jq
```

**Create a new book**
```bash
curl -X POST http://127.0.0.1:8000/api/books/ -H "Content-Type: application/json" -d '{
  "title": "Find Me",
  "author": "André Aciman",
  "isbn": "9780374155018",
  "published_date": "2019-10-29",
  "status": "available"
}'
```

**Get a single book**
```bash
curl http://127.0.0.1:8000/api/books/1/ | jq
```

**Update a book**
```bash
curl -X PUT http://127.0.0.1:8000/api/books/1/ -H "Content-Type: application/json" -d '{
  "title": "Call Me by Your Name (Updated)",
  "author": "André Aciman",
  "isbn": "9781250169440",
  "published_date": "2007-01-23",
  "status": "archived"
}'
```

**Delete a book**
```bash
curl -X DELETE http://127.0.0.1:8000/api/books/1/
```

---

## 3. Local Build & Run Instructions

**Clone the repo**
```bash
git clone https://github.com/egshiglen2024359/capstone-project.git
cd capstone-project
```

**Run with docker-compose**
```bash
docker-compose up --build
```

---

## 4. Running Tests Locally

If you run tests inside Docker:
```bash
docker-compose exec app pytest ./api/tests/test_views.py
```

If you run tests on your own machine (outside Docker), install dependencies first:
```bash
pip install -r requirements.txt
pytest ./api/tests/test_views.py
```

---

## 5. CI/CD Pipeline Explanation
This project uses a multi-stage GitHub Actions workflow to test, build, and deploy the application.

When I push changes or open a pull request to `main`:

1. **Run the unit tests** — checks out the code, installs dependencies, and runs `pytest` to make sure the app works.
2. **Run migrations** — applies Django migrations to verify the database schema is up-to-date.
3. **Check for missing migrations** — runs `python manage.py makemigrations --check` to ensure no untracked model changes.
4. **Semantic release** — if tests and migrations pass, uses `semantic-release` to determine a new version based on commit messages, update the changelog, and tag the release.
5. **Build and push Docker image** — logs in to GHCR, builds the image with the new semantic version tag, and pushes it to `ghcr.io/egshiglen2024359/capstone-project`.
6. **Update Helm values** — automatically updates `environments/production/values.yaml` with the new image tag and commits it to `main`.
7. **Argo CD auto-sync** — because my cluster is connected to this repo with Argo CD, it detects the change to `values.yaml` and automatically deploys the new version of the app to Kubernetes.

**Note on image tag:** In Helm, I explicitly override `image.tag` in `values.yaml` so Argo CD deploys the exact version that was built in CI (instead of using `.Chart.AppVersion`).

---

## 6. Kubernetes & Helm Setup Instructions

**Create a local cluster (k3d example)**
```bash
k3d cluster create capstone-cluster --port "8081:80@loadbalancer" --port "8443:443@loadbalancer" --port "30000-30010:30000-30010@server:0"
```

**Install PostgreSQL**
```bash
helm install books-database oci://registry-1.docker.io/bitnamicharts/postgresql -f postgres-values.yaml -n default
```

**Add secret to pull my Docker image**
```bash
kubectl create secret docker-registry ghcr-token --docker-server=ghcr.io --docker-username=egshiglen2024359 --docker-password=<TOKEN> --docker-email=2024359@student.cct.ie -n default
```

**Deploy the app**
```bash
helm upgrade --install books-catalog-app ./books-catalog-chart 
```

**Check it’s running**
```bash
kubectl get pods -n default
kubectl get svc -n default
```

---

## 7. Argo CD Setup (GitOps Deployment)

For Kubernetes deployments to sync automatically from this repo, use **Argo CD**.

**Add Argo CD Helm repo and install** (if not already installed):
```bash
helm repo update
helm repo add argo https://argoproj.github.io/argo-helm
helm install argocd argo/argo-cd -n argocd -f argocd-values.yaml
```

**Port-forward the Argo CD server to log in locally:**
```bash
kubectl port-forward service/argocd-server -n argocd 8080:443
```

Open your browser at:
```
http://localhost:8080/argocd
```

**Or Use ingress controller and access ArgoCD externally:** (No need for port-forwarding)
```
http://localhost:8081/argocd
```

**Get the admin password:**
```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

**Create an Application in Argo CD** pointing to:
- **Repo URL:** `https://github.com/egshiglen2024359/capstone-project`
- **Sync Policy:** `Automated`
- **Revision:** `main`
- **Path:** `books-catalog-chart`
- **Cluster URL:** `https://kubernetes.default.svc`
- **Namespace:** `default`
- **Value Files:** `environments/production/values.yaml`
- **Remove image tag override**

Once synced, Argo CD will watch this repo and keep Kubernetes deployment up to date automatically with the latest image tag.

## 📘 Summary
This project showcases **end-to-end DevOps delivery**:
Code → Test → Build → Version → Deploy → Sync → Monitor


## 👩‍💻 Author
**Egshiglen Enkhbayar**  
📍 Dublin, Ireland  
🔗 [GitHub](https://github.com/egshiglen-henny) | [LinkedIn](https://linkedin.com/in/egshiglene)
