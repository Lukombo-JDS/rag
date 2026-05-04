from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    Question: str

@app.get("/test")
def hello():
    return {"message": "Hello World !"}


@app.get("/health")
def health():
    return {"message": "Ok"}


@app.post("/request/")
async def request(request: Request):
    return request

@app.post("/uploadFile/")
async def create_upload_file(file: UploadFile)
    return {"filename": file.filename}
