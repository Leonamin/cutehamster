from typing import Optional
import uuid
import base64
from datetime import datetime
import os
import shutil
from fastapi import UploadFile

from app import database
from app.core import config
from app.model import model


def save_file(file: UploadFile, base_dir: str):
    now = datetime.now()
    folder_path = os.path.join(base_dir, str(
        now.year), str(now.month), str(now.day))

    os.makedirs(folder_path, exist_ok=True)

    # 파일의 고유한 이름 생성
    file_extension = file.filename.split(".")[-1]
    file_uuid = generate_base64_filename()
    file_name = f"{file_uuid}.{file_extension}"
    file_path = os.path.join(folder_path, file_name)
    relative_path = os.path.normpath(os.path.relpath(file_path, base_dir))

    # 파일 저장
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return relative_path, file_uuid, file_extension


def generate_base64_filename():
    random_uuid = uuid.uuid4()
    encoded_name = base64.urlsafe_b64encode(random_uuid.bytes)
    filename = encoded_name.decode('utf-8')
    return filename


async def create_file_record(file_path: str, uuid: str, file_extension: str, file: UploadFile):
    try:
        db: database.SessionLocal = next(database.get_db())
        file_size = file.file.tell()

        now = int(datetime.now().timestamp())

        file_record = model.File(
            file_path=file_path,
            uuid=uuid,
            ext=file_extension,
            size=file_size,
            file_metadata=None,
            created_at=now
        )
        db.add(file_record)
        db.commit()
        db.refresh(file_record)
    except Exception as e:
        raise


async def get_file_path(uuid: str) -> Optional[str]:
    file: model.File = await get_file_record(uuid)

    base_dir = config.settings.BASE_DIR
    abs_file_path = os.path.join(base_dir, file.file_path)
    if (os.path.isfile(abs_file_path)):
        return abs_file_path


async def get_file_record(uuid: str):
    try:
        db: database.SessionLocal = next(database.get_db())
        file_record = db.query(model.File).filter(
            model.File.uuid == uuid).first()
        return file_record
    except Exception as e:
        raise
