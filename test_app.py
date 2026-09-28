from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
       response = client.get("/")
       assert response.status_code == 200
       assert response.json() == {"message": "Welcome to the Distributed Task Tracker API"}

def test_create_task():
       response = client.post("/tasks/", json={"title": "Study for Cloud Exam", "completed": False})
       assert response.status_code == 201
       assert response.json()["title"] == "Study for Cloud Exam"

def test_get_tasks():
       response = client.get("/tasks/")
       assert response.status_code == 200
       assert isinstance(response.json(), list)

def test_get_task_not_found():
       response = client.get("/tasks/999")
       assert response.status_code == 404
       assert response.json()["detail"] == "Task not found"