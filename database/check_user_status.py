import datetime
from configs import Config
from handlers.database import Database

db = Database(Config.DATABASE_URL, Flux)

async def handle_user_status(Client, Message):
    chat_id = Message.from_user.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await Client.send_message(
            Config.LOG_CHANNEL,
            f"#NEW_USER: \n\nNew User [{Message.from_user.first_name}](tg://user?id={Message.from_user.id}) started @FluxTrialBot !!"
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await Message.reply_text("You are Banned to Use This Bot 🥺", quote=True)
            return
    await Message.continue_propagation()
