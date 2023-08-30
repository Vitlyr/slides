from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, FileResponse, Response
from typing import Optional
from pydantic import BaseModel
from fastapi.params import Body
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configure CORS
origins = [
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

web = {}

# Add the staticfiles route

@app.get("/docs")
def home():
    return {"Data": "Test"}

@app.get("/")
def about():
  index_file = open("/config/index.html", "rb")
  contents = index_file.read()
  index_file.close()
  return FileResponse(contents)
