from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema

def create_task(db:Session, task_create:task_schema.TestCreate) -> task_model.Test:
    task = task_model.Test(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_with_done(db: Session):
    result: Result = db.execute(
        select(
            task_model.Test.id,
            task_model.Test.contentMain,
            task_model.Test.time,
            task_model.Test.tag,
            task_model.Test.score
        )
    )
    return result.all()