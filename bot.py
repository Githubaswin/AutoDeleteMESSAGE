import asyncio
from os import environ
from pyrogram import Client, filters, idle

# Your API_ID, API_HASH, and BOT_TOKEN remain unchanged
API_ID = 26229903
API_HASH = environ.get("b5197d148bd3665a1eb45d1d18b02ad3")
BOT_TOKEN = environ.get("AAEx9nVNRKchWaLk01zeUBW7cgQ8vOpaFb0")
SESSION = environ.get("DDOgZ_iDJEf0LO4FlOpYQgcrAz93NsWpomywxamFIibYODav5otIcr_dIbhzoyof6DzoYGdQYM5LivU9PZfdeLPNHWFj")
TIME = 300

# Initialize GROUPS and ADMINS lists with default values
GROUPS = [-1001683780889, -1001800005463, -1001658506865]
ADMINS = [503170505]

# Check if "GROUPS" environment variable is set
groups_env = environ.get("GROUPS")
if groups_env:
    for grp in groups_env.split():
        GROUPS.append(int(grp))
else:
    print("Warning: 'GROUPS' environment variable not set or empty.")

# Check if "ADMINS" environment variable is set
admins_env = environ.get("ADMINS")
if admins_env:
    for usr in admins_env.split():
        ADMINS.append(int(usr))
else:
    print("Warning: 'ADMINS' environment variable not set or empty.")

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
