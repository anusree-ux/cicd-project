# CI/CD Pipeline for a Flask Application

A DevOps project demonstrating a complete CI/CD pipeline for a containerized Flask application using Jenkins, Docker, and Kubernetes (Kind).

## Technologies

* Python & Flask
* Pytest
* Git & GitHub
* Jenkins
* Docker
* Kubernetes (Kind)
* GitHub Webhooks

## Pipeline Workflow

1. Push code to GitHub
2. Jenkins is triggered automatically via GitHub Webhook
3. Install dependencies
4. Run unit tests
5. Build Docker image
6. Load image into Kind cluster
7. Deploy to Kubernetes
8. Verify deployment

## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Run Tests

```bash
pytest -v
```

## Author

**Anusree Manoj**

