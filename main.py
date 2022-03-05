from pyrogram import filter, Client

Client = Client("my_account")
@Client.on_message(filters.private)
async def hello(Client, message ):
    await message.reply("Hello")
    
Client.run()
