# Kubernetes Beginner Demo

This is a simple beginner-friendly Kubernetes project.  
It deploys a small Python Flask application to a local Minikube cluster.

## What this project contains

- A small Flask web app (`app.py`)
- A Dockerfile to build the image
- Kubernetes YAML files:
  - Namespace
  - Deployment
  - Service

## How to run this project

### 1. Start Minikube

minikube start --driver=docker

### 2. Build Docker image inside Minikube

eval $(minikube docker-env)
docker build -t k8s-beginner-demo:v1 ./app

### 3. Apply Kubernetes files

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

### 4. Check resources

kubectl get pods -n demo-app
kubectl get svc -n demo-app

### 5. Access the app
Option 1 – Using Minikube:

minikube service k8s-beginner-demo-svc -n demo-app

### Option 2 – Using port-forward:

bash
Copy code
kubectl port-forward -n demo-app deploy/k8s-beginner-demo 8080:5000

http://localhost:8080/

### Project Structure

k8s-beginner-demo/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── k8s/
    ├── namespace.yaml
    ├── deployment.yaml
    └── service.yaml
Done ✔️
This is a simple project.
