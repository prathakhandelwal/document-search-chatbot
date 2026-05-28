from fastapi import FastAPI
from app.routes import documents_routes

app=FastAPI()

app.include_router(documents_routes.router)

@app.get("/")
def health():
    return {"status": "running"}
