from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.cruds.task as task_crud
from api.db import get_db

import api.schemas.task as task_schema

router = APIRouter()

@router.get("/api/v1/tasks", response_model=list[task_schema.Test])
async def list_tasks(db: Session=Depends(get_db)):
    return task_crud.get_tasks_with_done(db)

@router.post("/api/v1/tasks", response_model=task_schema.TestCreateResponse)
async def create_task(task_body: task_schema.TestCreate, db: Session=Depends(get_db)):
    return task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass