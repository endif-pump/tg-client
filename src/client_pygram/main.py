import os
import time
import logging

from pyrogram import Client
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('logger')

load_dotenv()

api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
user_tag = os.getenv('user_tag')

client = Client(name="my_account", api_hash=api_hash, api_id=api_id)

@client.on_message(filters.private)
def type(client_object, message: Message):
        logger.info("Работаем")
        time.sleep(3)
        count = 1
        for dialog in client.get_dialogs():
                if dialog.chat.id == message.chat.id:
                        count = dialog.unread_messages_count
                        
        if not message.outgoing and count > 0:
                
                time.sleep(2)
                client.send_message(user_tag, "Пришло сообщение")
                logger.info("Уведомление отправлено")
        elif count == 0:
                logger.info("Проигнорировано, так как сообщение прочитано вами")

        else:
                logger.info("Проигнорировано, так как сообщение ваше")
        

client.run()
