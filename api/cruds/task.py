from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db:Session, task_create:task_schema.user) -> task_model.User:
    task = task_model.User(**task_create.dict())
    db.add(task) # DB에 튜플 추가 (저장이 안된 상태)
    db.commit() # DB의 트랜잭션 반영하기 (저장)
    db.refresh(task) # DB 새로고침 (중요합니다.)
    return task

def get_tasks_with_done(db: Session):
    result: Result = db.execute(
        select(
            task_model.User.user_nickname,
            task_model.User.email,
            task_model.User.password,
            task_model.User.mobile_number,
            task_model.User.login_at,   
            task_model.User.logout_at,
            task_model.User.create_at,
            task_model.User.updated_at
        )
    )
    return result.all()


'''
    time / title / tag / emoji
'''