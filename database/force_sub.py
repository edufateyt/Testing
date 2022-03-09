import asyncio
from typing import Union
from config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

async def get_invite_link(Client, chat_id: Union[str, int]):
    try:
        invite_link = await Client.create_chat_invite_link(chat_id=chat_id)
        return invite_link
    except FloodWait as e:
        print(f"Sleep of {e.x}s caused by FloodWait ...")
        await asyncio.sleep(e.x)
        return await get_invite_link(Client, chat_id)


async def handle_force_sub(Client, Message):
    if Config.UPDATES_CHANNEL and Config.UPDATES_CHANNEL.startswith("-100"):
        channel_chat_id = int(Config.UPDATES_CHANNEL)
    elif Config.UPDATES_CHANNEL and (not Config.UPDATES_CHANNEL.startswith("-100")):
        channel_chat_id = Config.UPDATES_CHANNEL
    else:
        return 200
    try:
        user = await Client.get_chat_member(chat_id=channel_chat_id, user_id=Message.from_user.id)
        if user.status == "kicked":
            await Client.send_message(
                chat_id=Message.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/FluxSupport).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await get_invite_link(Client, chat_id=channel_chat_id)
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await Client.send_message(
            chat_id=Message.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!\n\nDue to Overload, Only Channel Subscribers can use the Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url= "t.me/themalwarezone")
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await Client.send_message(
            chat_id=Message.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/FluxSupport).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 200
    return 200
