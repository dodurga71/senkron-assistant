from pydantic import BaseModel

class IncomingMessage(BaseModel):
    user_id: str
    text: str
    timestamp: str
