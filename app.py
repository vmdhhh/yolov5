from fastapi import FastAPI
import deploy_api

app = FastAPI()
app.include_router(deploy_api.router, prefix='/yolo')


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'YOLO is all ready to go!'