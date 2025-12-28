from fastapi import FastAPI, Form
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/request")
async def req(
    u: str = Form(...),
    m: str = Form(...),
    p: str = Form(...)
):
    response = ""
    parms = json.loads(p) if p else None
    if m.upper() == "GET":
        response = requests.get(u, params=parms)
    elif m.upper() == "POST":
        response = requests.post(u, params=parms)
    elif m.upper() == "PUT":
        response = requests.put(u, params=parms)
    elif m.upper() == "DELETE":
        response = requests.delete(u, params=parms)
    data = response.json()
    return f'{data}'

