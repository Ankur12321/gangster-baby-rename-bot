import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5971971751:AAEJYE9EGQw7RvtLE1dluzSifgLEy-HlvL4")

API_ID = int(os.environ.get("API_ID", "21970746"))

API_HASH = os.environ.get("API_HASH", "32deb816dc3874e871b6158673fd3683")

STRING = os.environ.get("STRING", "BQFPPzoAXoiiPd0cWdJ4k4M-vLUFTa63H4pHujHOYXvjXlK9oFTBoBwo6ilxuP7DmJ2TqpuPOkxCZMvK7MhIJQr-BBu3wGSweOGEXcI972OZ-iilInB1WKGVM8yzfCG2ce-Zu44i4yDLEQgguC1wYL8etbvKOYAKhnt-IRi8P9o-1v-saGHf37yZYcDtRwpCKvP6nw0ruQzJSs6L7Hh-cgZXqRTrWUU1RXJpO4AP-YDGSi8Kdsb9k3Uea3cxB0kkYv7YfHEEU_3HscxwEhEGz-9woTByJgomGETuNcv62o-QoBf_lUvq0J5iciBDxeNnLA-ogGPyweMfs7gEwP_J9SFCfu0p9gAAAAB2c6InAA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
