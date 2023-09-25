import asyncio
from os import environ
from pyrogram import Client, filters, idle


API_ID = 1417176
API_HASH = environ.get("e2247341eeec70b41e0e04fc605bd864")
BOT_TOKEN = environ.get("AAEx9nVNRKchWaLk01zeUBW7cgQ8vOpaFb0")
SESSION = environ.get("DDOgZ_iDJEf0LO4FlOpYQgcrAz93NsWpomywxamFIibYODav5otIcr_dIbhzoyof6DzoYGdQYM5LivU9PZfdeLPNHWFj")
TIME = int(environ.get("300"))
GROUPS = [-1001683780889 -1001393812865 -1001658506865]
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = [503170505]
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time Join our Ofiicial Channel @T4TVSeries1</b>"


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

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
