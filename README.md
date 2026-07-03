# CI/CD Pipeline for a Flask Application

This project demonstrates an end-to-end CI/CD pipeline for a Flask web application using Jenkins, Docker, and Kubernetes (Kind). Every push to the GitHub repository automatically triggers a Jenkins pipeline via GitHub Webhooks, which runs tests, builds a Docker image, and deploys the application to a Kubernetes cluster.

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
3. Jenkins checks out the latest code.
4. Dependencies are installed.
5. Unit tests are executed using Pytest.
6. A Docker image is built.
7. The image is loaded into the Kind cluster.
8. Deployed to Kubernetes
9. Jenkins verifies the deployment.

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
