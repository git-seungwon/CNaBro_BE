from fastapi import FastAPI
import os

from api.domain.user import user_routers
from api.domain.note import note_routers

app = FastAPI()

@app.get("/version")
def root():
    return {"version": os.getenv("version")}

app.include_router(user_routers.router)
app.include_router(note_routers.router)