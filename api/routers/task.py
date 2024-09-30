from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.cruds.task as task_crud
from api.db import get_db

import api.schemas.task as task_schema

router = APIRouter(
    prefix="/api/v1"
)

@router.get("/tasks", response_model=list[task_schema.user])
async def list_tasks(db: Session=Depends(get_db)):
    return task_crud.get_tasks_with_done(db)

@router.post("/tasks", response_model=task_schema.user_Create_Response)
async def create_task(task_body: task_schema.userCreate, db: Session=Depends(get_db)):
    return task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass