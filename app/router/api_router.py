from fastapi import APIRouter

from app.file.router import router as FileRouter

router = APIRouter(
    prefix="/api",
)

router.include_router(FileRouter)
