from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("26084567"))
API_HASH = input("3cf13649bbf0e931e40fde340768bb64") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
