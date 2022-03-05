import asyncio
from pyrogram import filters, Client
from config import Config

Flux = Client("Test",
               api_id=Config.API_ID,
               api_hash=Config.API_HASH,
               bot_token=Config.BOT_TOKEN
          )
MENTION = "[{}](tg:user?id={})"
@Flux.on_message(filters.command(["start"]))
async def hello(client, message):
    await message.reply_text(text="Hello {}")

@Flux.on_message(filters.private & filters.text)
async def echo(client, message):
     await message.reply(message.text)
    
Flux.run()
