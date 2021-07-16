from fastapi import FastAPI, UploadFile, File
from detect_api import detect
from fastapi.responses import FileResponse
import shutil

app = FastAPI()

@app.post("/detect")
async def root(file: UploadFile = File(...)):
    with open(f'test_images/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    image = detect(source=file.filename)
    return FileResponse(image)

@app.get("/")
def new_function():
    return {"message": "Check /detect endpoint"}