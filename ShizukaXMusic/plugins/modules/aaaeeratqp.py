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



@app.on_message(filters.command(["مايسترو","بيكاسو"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/0a70df2f83175334042f1.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : »» [⏤͟͟͞𝘼𝙇-𝙈𝘼𝙀𝙎𝙏𝙍𝙊⚝➣⃟𝙈ِ°亗™↝⸀🇾🇪˼](https://t.me/FH_3B)
◉ 𝚄𝚂𝙴𝚁 : »» @FH_3B
◉ 𝙸𝙳   : »» 6274098601
◉ 𝙱𝙸𝙾  : »» **"أن لـم تـكـونـوا أوفـيـاء فلا تـعـبـثـوا بـقـلـوب الأنـقـيـاء...!! ✪!**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("⏤͟͟͞𓆩𝘼𝙇-𝙈𝘼𝙀𝙎𝙏𝙍𝙊⚝➣⃟𝙈ِ°亗™↝⸀🇾🇪˼", url=f"https://t.me/FH_3B"),
            ]
         ]
     )
  )

