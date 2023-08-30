from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configure CORS
origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the staticfiles route

@app.get("/docs")
def home():
    return {"Data": "Test"}

@app.get("/")
def about():
    file_path = "/config/static/index.html"
    with open(file_path, "r") as index_file:
        contents = index_file.read()
    return FileResponse(contents, media_type="text/html")