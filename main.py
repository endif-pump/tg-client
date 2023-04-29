import os

from telethon import TelegramClient, sync, events
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
user_tag = os.getenv('user_tag')
message = 'Вам пришло уведомление'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage())
async def normal_handler(event):
    entity = await client.get_entity(user_tag)
    await client.send_message(entity, message)

client.start()

client.run_until_disconnected()
