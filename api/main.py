import os

from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from api.domain.user import user_router
from api.domain.note import note_router

from langserve import add_routes
from api.domain.langchain.langchain_model import chain

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/version")
def root():
    return {"version": os.getenv("version")}

app.include_router(user_router.router)
app.include_router(note_router.router)

add_routes(app, chain, path="/chain", dependencies=[Depends(user_router.get_current_user)])   