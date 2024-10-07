from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/version")
def root():
    return {"version": os.getenv("version")}

@app.get("/")
def main():
    return {"message": "hello main_page!"}
