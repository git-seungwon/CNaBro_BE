from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db:Session, task_create:task_schema.TestCreate) -> task_model.Test:
    task = task_model.Test(**task_create.dict())
    db.add(task) # DB에 튜플 추가 (저장이 안된 상태)
    db.commit() # DB의 트랜잭션 반영하기 (저장)
    db.refresh(task) # DB 새로고침
    return task

def get_tasks_with_done(db: Session):
    result: Result = db.execute(
        select(
            task_model.Test.id,
            task_model.Test.time,
            task_model.Test.title,
            task_model.Test.tag,
            task_model.Test.emoji
        )
    )
    return result.all()


'''
    time / title / tag / emoji
'''