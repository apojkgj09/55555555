import asyncio
import os
from pyrogram.types import CallbackQuery
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ShizukaXMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(filters.command(["سايران","ريهام"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/6db1c9d437def988f483a.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : »» [⏤͟͟͞𝙎𝘼𝙔𝙍𝘼𝙉⇭⚝➣⃟𝙎](https://t.me/SA_YRAN)
◉ 𝚄𝚂𝙴𝚁 : »» @SA_YRAN
◉ 𝙸𝙳   : »» 6263359697
◉ 𝙱𝙸𝙾  : »» **ويـحاولـون دائـما لفـت انتبـاهـي لڪـني لا أبـالــي..!!**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("⏤͟͟͞𝙎𝘼𝙔𝙍𝘼𝙉⇭⚝➣⃟𝙎", url=f"https://t.me/SA_YRAN"),
            ]
         ]
     )
  )

