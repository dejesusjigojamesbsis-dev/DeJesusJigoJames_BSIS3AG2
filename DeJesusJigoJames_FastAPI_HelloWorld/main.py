from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Jigo De Jesus Hello World"}
