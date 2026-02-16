from fastapi import FastAPI
from app.api.generate_form import router as form_router

app = FastAPI(
    title="APISIX Schema Form Engine",
    version="0.1.0"
)

app.include_router(form_router)

@app.get("/")
def health_check():
    return {"status": "ok"}