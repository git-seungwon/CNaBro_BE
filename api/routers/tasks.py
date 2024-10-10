from fastapi import APIRouter, Depends
import os

router = APIRouter()

@router.get("/version")
async def get_version():
    return {"version": os.getenv("version")}

    