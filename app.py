from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Task Tracker API")
tasks_db = []
task_id_counter = 1

class Task(BaseModel):
       title: str
       completed: bool = False

@app.get("/")
def read_root():
       return {"message": "Welcome to the Distributed Task Tracker API"}

@app.post("/tasks/", status_code=201)
def create_task(task: Task):
       global task_id_counter
       new_task = task.dict()
       new_task["id"] = task_id_counter
       task_id_counter += 1
       tasks_db.append(new_task)
       return new_task

@app.get("/tasks/", response_model=List[dict])
def get_tasks():
       return tasks_db

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
       for task in tasks_db:
           if task["id"] == task_id:
               return task
       raise HTTPException(status_code=404, detail="Task not found")