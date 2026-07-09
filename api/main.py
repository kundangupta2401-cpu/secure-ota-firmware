from fastapi import UploadFile, File
import shutil
import subprocess
import os
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Secure OTA Dashboard")

app.mount("/static", StaticFiles(directory="api/static"), name="static")

templates = Jinja2Templates(directory="api/templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "firmware_version": "1.0.0",
            "server_status": "ONLINE",
            "device_status": "CONNECTED",
            "signature_status": "SIGNED"
        }
    )
@app.post("/generate_keys")
def generate_keys():

    result = subprocess.run(
        ["python", "generate_keys.py"],
        cwd="signing",
        capture_output=True,
        text=True
    )

    return JSONResponse({
        "status": "success",
        "message": result.stdout
    })
@app.post("/sign_firmware")
def sign_firmware():

    result = subprocess.run(
        ["python", "sign_firmware.py"],
        cwd="signing",
        capture_output=True,
        text=True
    )

    return JSONResponse({
        "status": "success",
        "message": result.stdout
    })
@app.post("/verify_firmware")
def verify_firmware():

    result = subprocess.run(
        ["python", "verify_firmware.py"],
        cwd="signing",
        capture_output=True,
        text=True
    )

    return JSONResponse({
        "status": "success",
        "message": result.stdout
    })
@app.post("/install_firmware")
def install_firmware():

    result = subprocess.run(
        ["python", "install_firmware.py"],
        cwd="edge_agent",
        capture_output=True,
        text=True
    )

    return JSONResponse({
        "status": "success",
        "message": result.stdout
    })
@app.post("/upload_firmware")
async def upload_firmware(file: UploadFile = File(...)):

    save_path = f"firmware/uploads/{file.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": f"{file.filename} uploaded successfully!"
    }