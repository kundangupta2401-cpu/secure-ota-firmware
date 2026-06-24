from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Secure OTA Server Running"
    }