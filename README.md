# Cloud Mini-Project: Distributed Task Tracker API

A lightweight, containerized RESTful API built with FastAPI, designed to manage tasks. This project demonstrates modern cloud deployment practices, including CI/CD automation and containerization.

## 🚀 Features
- **FastAPI Backend**: High-performance Python web framework with automatic data validation using Pydantic.
- **Automated Testing**: 4 comprehensive `pytest` cases ensuring reliability (happy paths and edge cases).
- **CI/CD Pipeline**: GitHub Actions workflow that automatically runs tests and **blocks merging** if any test fails.
- **Containerization**: Packaged with Docker for consistent environments across local and cloud machines.
- **Cloud Deployment**: Hosted live on an AWS EC2 instance (Ubuntu), pulled directly from Docker Hub.

## 🛠️ Tech Stack
- Python 3.11, FastAPI, Uvicorn, Pydantic
- Docker & Docker Hub
- GitHub Actions (CI/CD)
- AWS EC2 (Free Tier)

## 🌐 Live Demo
- **API Endpoint**: `http://13.51.162.155` 
- Try it: `curl http://13.51.162.155/`

## 📦 How to Run Locally
1. Clone the repository: `git clone https://github.com/bhaskarthakur07/cloud-mini-project.git`
2. Build the Docker image: `docker build -t task-api .`
3. Run the container: `docker run -d -p 80:80 task-api`
4. Visit `http://localhost` in your browser.

## 🛡️ Branch Protection
This repository is configured to require the `test` status check to pass before any code can be merged into the `main` branch, ensuring production stability.
