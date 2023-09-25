import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = []
API_HASH = environ.get("")
BOT_TOKEN = environ.get("")
SESSION = environ.get("")
TIME = 300
GROUPS = []

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time. Join our Official Channel @T4TVSeries1</b>"

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )

Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )

@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

# The code below will not be reached unless you forcefully stop the script

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
