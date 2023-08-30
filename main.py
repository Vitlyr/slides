from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, Response
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
    with open("config/static/index.html") as f:
        content = f.read()
    with open("config/static/script.js") as js_file:
        js_content = js_file.read()
        content_with_js = content.replace("</body>", f"<script>{js_content}</script></body>")
        return HTMLResponse(content=content_with_js, media_type="text/html")
