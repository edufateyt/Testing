import asyncio
from pyrogram import filter, Client

Flux = Client("Test",
               api_id=config.API_ID,
               api_hash=config.API_HASH,
               bot_token=config.BOT_TOKEN
          )

@Flux.on_message(filters.command(["start"]))
async def hello(client, message):
    await update.reply_text(text="Hello Brother")
    
Flux.run()
