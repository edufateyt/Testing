import asyncio
from pyrogram import filters, Client
from config import Config
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
Flux = Client("Test",
               api_id=Config.API_ID,
               api_hash=Config.API_HASH,
               bot_token=Config.BOT_TOKEN
          )

@Flux.on_message(filters.command(["start"]))
async def hello(client, message):
    await message.reply_text(text="👋 Hi There!\n\nThis Bot Is Made For Testing Purposes 🌀\n\n If You Want To Contribute, Help The Developer In Learning Pyrogram 🛠️.")

@Flux.on_message(filters.private & filters.text)
async def echo(client, message):
     await message.reply(message.text)
    
Flux.run()
