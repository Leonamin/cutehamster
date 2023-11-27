from typing import Optional
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse

from app.file import service
from app.core import config

from app.file import service
from app.file.schema import FileCreateResponse

router = APIRouter(
    prefix="/file",
    tags=['file']
)


@router.get('/{access_key}')
async def get_file(access_key: str):
    file_path: Optional[str] = await service.get_file_path(access_key)
    if file_path is None:
        return HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)


@router.post("", response_model=FileCreateResponse)
async def create_file(
    file: UploadFile = File(),
):
    base_dir: str = config.settings.BASE_DIR
    # 파일 저장
    file_path, file_uuid, file_extension = service.save_file(file, base_dir)

    await service.create_file_record(file_path, file_uuid, file_extension, file)

    return FileCreateResponse(access_key=file_uuid)


# @router.put('/{access_key}')
# async def update_file(access_key: str):
#     return {"access_key": access_key}


# @router.delete('/{access_key}')
# async def delete_file(access_key: str):
#     return {"access_key": access_key}
