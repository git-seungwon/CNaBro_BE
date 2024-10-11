from fastapi import FastAPI
import os

from api.domain.user import user_routers

app = FastAPI()

@app.get("/version")
def root():
    return {"version": os.getenv("version")}
@app.get("/")
def main():
    return {"message": "main_page!"}

app.include_router(user_routers.router)