<<<<<<< HEAD
# Docker Learning
=======
# Docker Learning 
>>>>>>> 3ff2883 (update readme)

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

## 🔍 Troubleshooting & Problem Solving

During this project, I encountered and resolved several real-world issues while building and deploying containerized applications.

| Challenge | Resolution |
|-----------|------------|
| **Container exited immediately after starting** | Used `docker ps -a` and `docker logs` to identify application startup errors, corrected the code, rebuilt the image, and verified the container started successfully. |
| **Flask couldn't communicate with Redis** | Configured both containers on the same Docker network and connected to Redis using the Compose service name (`my-redis`) instead of `localhost`. |
| **Redis data was lost when the container restarted** | Implemented a named Docker volume and enabled Redis AOF persistence to ensure data survived container recreation. |
| **Docker Compose configuration issues** | Fixed YAML indentation, corrected service dependencies, and modernized the Compose file by removing deprecated configuration. |
| **Docker Hub authentication issues** | Investigated Docker credential helper errors, understood how `pass` stores credentials securely on Linux, and configured authentication successfully. |
| **Amazon ECR authentication failed** | Configured the AWS CLI credentials, authenticated with Amazon ECR, tagged Docker images correctly, and pushed them to a private AWS registry. |
| **Nginx configuration mount failed** | Diagnosed a bind mount mismatch between a host file and container path, corrected the volume mapping, and successfully configured Nginx as a reverse proxy. |

---

## 🚀 Docker Skills Demonstrated

- Building custom Docker images with Dockerfiles
- Running and managing containers
- Creating multi-container applications with Docker Compose
- Docker networking and inter-container communication
- Persistent storage using Docker volumes
- Configuring Redis persistence
- Reverse proxy configuration with Nginx
- Debugging containers using `docker logs`, `docker ps`, and container inspection
- Publishing images to Docker Hub
- Publishing images to Amazon Elastic Container Registry (ECR)
- Authenticating Docker with registry credential helpers

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
