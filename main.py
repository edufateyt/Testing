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
async def hello(Client, message):
    await message.reply_text(
      text="👋 Hi There!\n\nThis Bot Is Made For Testing Purposes 🌀\n\n If You Want To Contribute, Help The Developer In Learning Pyrogram 🛠️.",
      reply_markup = InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("Click", callback_data = "testing")
        ]
      ]
      
  )
      
@Flux.on_callback_query()
async def button(Flux: Client,cmd: CallbackQuery):
data = cmd.data
if "testing" in data:
await CallbackQuery.message.edit("Thanks For Trying")
      
Flux.run()
