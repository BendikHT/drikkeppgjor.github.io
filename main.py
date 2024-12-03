
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse


app = FastAPI()
app.mount("/", StaticFiles(directory="static",html = True), name="static")

@app.get("/")
def index():
    return FileResponse('index.html')

