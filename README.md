# Cute Hamster
겨울을 지내기위해 도토리를 저장하는 햄스터같이 파일을 저장하자.

## 파이썬 실행환경
1. python -m venv .venv
2. .\venv\Sripts\Activate.ps1 (Windows)
3. (venv 환경에서) pip install -r requirements.txt

## 서버 실행에 필요
1. 프로젝트 폴더에 `.env`를 생성하고 아래 내용을 작성한다
```
PROJECT_NAME="Cute Hamster"
VERSION="0.0.1"
ENVIRONMENT="dev"

DATABASE_URL="sqlite:////etc/server_storage/cutehamster_storage.db"
BASE_DIR="/etc/server_storage"
```
- **ENVIRONMENT**: 서버 환경, 아직 dev, test, prod에 따라 다른 설정은 없고 스웨거 활성화 여부만 달라진다.
- **DATABASE_URL**: 서버 DB 위치 현재 SQLite를 사용하고 있다. SQLite므로 로컬 파일 위치를 지정하면 된다.
- **BASE_DIR**: 서버에서 파일을 저장할 루트 폴더 위치
## 서버 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000

## 번외
- 라이브러리가 추가되거나 변경사항이 생긴다면 **requirements.txt**를 업데이트 해주자(`pip freeze > file_name` 나는 `pip freeze > requirements.txt`)
- DB는 별도 연결 없이 SQLite를 사용중 main파일을 실행하면 `model.Base.metadata.create_all(bind=engine)` 코드가 실행되서 cutehamster.db 파일이 생긴다