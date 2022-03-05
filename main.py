import asyncio
from pyrogram import filters, Client
from config import Conig

Flux = Client("Test",
               api_id=Config.API_ID,
               api_hash=Config.API_HASH,
               bot_token=Config.BOT_TOKEN
          )

@Flux.on_message(filters.command(["start"]))
async def hello(client, message):
    await update.reply_text(text="Hello Brother")
    
Flux.run()
