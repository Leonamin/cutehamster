from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.model import model
from app.database import engine
from app.file.router import router


def get_application():
    app_configs = {"title": settings.PROJECT_NAME, "version": settings.VERSION}

    if settings.ENVIRONMENT not in settings.SHOW_DOCS_ENVIRONMENT:
        app_configs["openapi_url"] = None

    _app = FastAPI(**app_configs)

    model.Base.metadata.create_all(bind=engine)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 추가할 라우터가 있으면 여기에 추가
    _app.include_router(router)

    return _app


app = get_application()
