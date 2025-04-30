from fastapi import APIRouter
from app.services.responder import auto_respond_if_timeout
from app.models.message_schema import IncomingMessage

router = APIRouter()

@router.post("/incoming-message")
async def receive_message(payload: IncomingMessage):
    await auto_respond_if_timeout(payload)
    return {"status": "received"}
