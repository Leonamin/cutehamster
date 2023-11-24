from fastapi import APIRouter


router = APIRouter(
    prefix="/file",
    tags=['file']
)


@router.get('/{uuid}')
async def get_file(uuid: str):
    return {"uuid": uuid}


@router.post('')
async def create_file():
    return {"result": "success"}


@router.put('/{uuid}')
async def update_file(uuid: str):
    return {"uuid": uuid}


@router.delete('/{uuid}')
async def delete_file(uuid: str):
    return {"uuid": uuid}
