import asyncio
from app.services.gpt_engine import generate_reply
from app.db.mongodb import store_reply, store_message

async def auto_respond_if_timeout(message):
    await store_message(message.dict())
    await asyncio.sleep(60)
    if not message_already_replied(message):
        reply = await generate_reply(message.text)
        await store_reply(message.user_id, reply)

def message_already_replied(message):
    return False
