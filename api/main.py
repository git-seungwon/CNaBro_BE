from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/version")
def root(): # test code
    return {"version": os.getenv("version")}
