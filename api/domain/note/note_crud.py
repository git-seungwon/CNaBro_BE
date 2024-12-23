from datetime import datetime
from sqlalchemy import select, func

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from api.models.ORM import Note, User
from api.domain.note import note_schema

async def upload_note(note:Note):
    ''' upload note content to vector store '''
    pass

async def search_notes(db: AsyncSession, user: User, skip: int = 0, limit: int = 10, keyword: str = ''):
    query = select(Note).filter(Note.user_id == user.user_id)
    
    if keyword:
        query = query.where(Note.content.contains(keyword))
    
    count_query = select(func.count()).select_from(query.subquery())
    total = (await db.execute(count_query)).scalar_one()
    
    note_list = await db.execute(query.offset(skip).limit(limit)
                                     .order_by(Note.create_at.desc())
                                     .distinct())
    
    return total, note_list.scalars().all()

async def get_note(db: AsyncSession, note_id: int):
    qeustion = await db.execute(select(Note).filter(Note.id == note_id))
    return qeustion.scalar_one_or_none()

async def create_note(db: AsyncSession, note_create: note_schema.NoteCreate, user: User):
    db_note = Note(
        content=note_create.content, 
        start_time=note_create.start_time,
        end_time=note_create.end_time,
        user_id=user.user_id
        )
    
    db.add(db_note)
    await db.commit()
    await db.refresh(db_note)

async def update_note(db: AsyncSession, db_note: Note, note_update: note_schema.NoteUpdate):  
    db_note.content = note_update.content
    db_note.update_at = datetime.now()
    db.add(db_note)
    await db.commit()
    await db.refresh(db_note)

async def delete_note(db: AsyncSession, db_note: Note):
    await db.delete(db_note)
    await db.commit()