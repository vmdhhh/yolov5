from fastapi import FastAPI, UploadFile, File, APIRouter
from detect_api import detect
from fastapi.responses import FileResponse
import shutil


router = APIRouter()

@router.post("/detect")
async def root(file: UploadFile = File(...)):
    with open(f'test_images/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = detect(source=file.filename)
    return FileResponse(image)

