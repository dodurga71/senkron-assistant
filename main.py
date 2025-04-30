from message_router import router as message_router
from fastapi import FastAPI
from app.routes.message_router import router as message_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SENKRON AI Assistant is running."}

app.include_router(message_router)
