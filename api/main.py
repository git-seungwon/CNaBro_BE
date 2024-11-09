from fastapi import FastAPI
import os

from api.domain.user import user_router
from api.domain.note import note_router

app = FastAPI()

@app.get("/version")
def root():
    return {"version": os.getenv("version")}

app.include_router(user_router.router)
app.include_router(note_router.router)