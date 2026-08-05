# Docker Learning

A collection of Docker projects and exercises completed while learning containerization, Docker Compose, networking, persistent storage, and container registries.

## 📚 About

This repository documents my journey learning Docker by building practical projects and exploring the Docker ecosystem, from writing Dockerfiles to publishing images in cloud registries.

## 🚀 Projects

### Hello Flask

A simple Flask application containerized with Docker.

**Concepts covered**

- Dockerfile
- Docker images
- Port mapping
- Docker Compose
- Container lifecycle

---

### Hello Redis

A Flask application connected to a Redis database.

**Features**

- Redis-backed page view counter
- Persistent storage using Docker Volumes
- Multi-container application with Docker Compose
- Custom Docker networking
- Nginx reverse proxy
- Published to Docker Hub
- Published to Amazon Elastic Container Registry (ECR)

## 🧰 Technologies Used

- Docker
- Docker Compose
- Python
- Flask
- Redis
- Nginx
- Amazon ECR
- Docker Hub
- Git & GitHub

## ☁️ Container Registries

As part of this project, I learned how to publish Docker images to different registries.

### Docker Hub

- Built Docker images
- Tagged images
- Authenticated with Docker Hub
- Pushed images successfully

Example:

```bash
docker build -t hello-redis .
docker tag hello-redis <dockerhub-username>/hello-redis:latest
docker push <dockerhub-username>/hello-redis:latest
```

### Amazon Elastic Container Registry (ECR)

- Created an ECR repository
- Authenticated using the AWS CLI
- Tagged Docker images
- Pushed images to Amazon ECR

Example:

```bash
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.eu-west-1.amazonaws.com

docker tag hello-redis:latest <account-id>.dkr.ecr.eu-west-1.amazonaws.com/hello-redis:latest

docker push <account-id>.dkr.ecr.eu-west-1.amazonaws.com/hello-redis:latest
```

## 📖 Skills Demonstrated

- Writing Dockerfiles
- Building Docker images
- Running containers
- Docker networking
- Docker Compose
- Docker volumes
- Redis persistence
- Nginx configuration
- Debugging container issues
- Docker Hub image publishing
- Amazon ECR image publishing
- Git version control

## 🎯 Next Steps

- Deploy the containers to AWS ECS
- Learn Kubernetes
- Add CI/CD with GitHub Actions
- Monitor containers using Prometheus and Grafana
