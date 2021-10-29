from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.sign import *
from app.config import *
from pydantic import BaseModel
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

class PosItem(BaseModel):
    longitude: str
    latitude:str

app = FastAPI()

origins = [
    "http://localhost:8081",
]
app.mount("/public", StaticFiles(directory="public/"), name="public")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/sign')
async def sign():
    result = await local_run()
    return result


@app.get('/qr_sign')
async def qr_sign(enc: str):
    result = await qcode_run(enc)
    return result


@app.get('/config')
def get_config():
    return USER_INFOS


@app.get('/pos')
def get_pos():
    return {"name": position, "longitude": longitude, "latitude": latitude}

@app.get("/")
async def get_index():
    return FileResponse('public/index.html')


@app.get("/{whatever:path}")
async def get_static_files_or_404(whatever):
    # try open file for path
    file_path = os.path.join("public", whatever)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse('public/index.html')



