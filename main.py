import asyncio
from pyrogram import filters, Client
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from database.database import db
from database.add_user_to_db import add_user_to_db
from database.check_user_status import handle_user_status
from database.force_sub import (handle_force_sub, get_invite_link)

Flux = Client("Test",
               api_id=Config.API_ID,
               api_hash=Config.API_HASH,
               bot_token=Config.BOT_TOKEN
          )
@Flux.on_message(filters.command(["start"]))
async def start(Client, Message):
  
    if Config.UPDATES_CHANNEL is not None:
        back = await handle_force_sub(Client, Message)
        if back == 400:
            return
          
    usr_cmd = Message.text.split("_", 1)[-1]
    if usr_cmd == "/start":
        await add_user_to_db(Client, Message)
        await Message.reply_text(
            text="**👋 Hi There!\n\nThis Bot Is Made For Testing Purposes.\n\n If You Want To Contribute, Help The Developer In Learning Pyrogram.**",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
              [
                [InlineKeyboardButton('Developer', url='t.me/TheMalwareAwakens'), InlineKeyboardButton('Bots', url='t.me/TheMalwareZone')],
                [InlineKeyboardButton('Custom', callback_data='custom')]
              ]
            )
        )

@Flux.on_callback_query()
async def button(Client, CallbackQuery):
  data = CallbackQuery.data
  if 'custom' in data:
    await CallbackQuery.message.edit(
      text= "**Yepp, It Works!**",
      parse_mode = "Markdown",
      disable_web_page_preview = True,
      reply_markup = InlineKeyboardMarkup(
        [
          [ InlineKeyboardButton('Channel', url = 't.me/Fluxbots')]
        ]
      )
    )
  elif "refreshForceSub" in data:
    if Config.UPDATES_CHANNEL:
      if Config.UPDATES_CHANNEL.startswith("-100"):
        channel_chat_id = int(Config.UPDATES_CHANNEL)
      else:
        channel_chat_id = Config.UPDATES_CHANNEL
        try:
          user = await Client.get_chat_member(channel_chat_id, cmd.message.chat.id)
          if user.status == "kicked":
            await Message.message.edit(
              text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/FluxSupport).",
              parse_mode="markdown",
              disable_web_page_preview=True
            )
            return
          except UserNotParticipant:
            invite_link = await get_invite_link(channel_chat_id)
            await Message.message.edit(
              text="**You Still Didn't Join ☹️, Please Join My Updates Channel to use this Bot!**\n\n"
              "Due to Overload, Only Channel Subscribers can use the Bot!",
              reply_markup=InlineKeyboardMarkup(
                [
                  [
                      InlineKeyboardButton("🤖 Join Updates Channel", url="TheMalwareZone")
                  ],
                  [
                      InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                  ]
                ]
              ),
              parse_mode="markdown"
            )
                
   
@Flux.on_message(filters.command(["photo"]))
async def start(Client, message):
  await message.reply_photo(
    photo = "https://telegra.ph/file/1c0e843d1d9206257b3ce.png",
    caption="My Owner's PFP"
  )
@Flux.on_message(filters.command(["doc"]))
async def start(Client, message):
  await message.reply_document(
    document ='https://telegra.ph/file/1c0e843d1d9206257b3ce.png',
    caption="My Owner's PFP"
  )  
@Flux.on_message(filters.private)
async def echo(Client, message):
  await message.reply(message.text)
  
Flux.run()
