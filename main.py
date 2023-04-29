from telethon import TelegramClient, sync, events

api_id = 1
api_hash = ''
user_tag = ''
message = 'Вам пришло уведомление'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage())
async def normal_handler(event):
    dialogs = await client.get_dialogs()
    entity = await client.get_entity(user_tag)
    await client.send_message(entity, message)

client.start()

client.run_until_disconnected()
