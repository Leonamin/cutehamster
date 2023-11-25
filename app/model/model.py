from sqlalchemy import BigInteger, Column, Integer, String

from ..database import Base


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, name="id", primary_key=True, index=True)
    file_path = Column(String, name="file_path", doc="파일이 운영체제에 저장된 절대경로")
    uuid = Column(String, name="uuid",
                  doc="파일 UUID file_path와 1:1 매칭", index=True, unique=True)
    ext = Column(String, name="ext", doc="파일 확장자 소문자")
    size = Column(BigInteger, name="size", doc="파일 크기")
    file_metadata = Column(String, name="file_metadata",
                           doc="JSON 형태의 메타데이터, 추후에 확장용도로 사용될 수 있음", nullable=True)
    created_at = Column(BigInteger, name="created_at", doc="파일 생성 시간")
    updated_at = Column(BigInteger, name="updated_at",
                        doc="파일 수정 시간", nullable=True)
    deleted_at = Column(BigInteger, name="deleted_at",
                        doc="파일 삭제 시간", nullable=True)
