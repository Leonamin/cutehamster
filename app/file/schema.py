from pydantic import BaseModel


class FileCreateResponse(BaseModel):
    access_key: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "access_key": "OwVBnSsgQUqS6-VKcl1Iwg=="
            }
        }
