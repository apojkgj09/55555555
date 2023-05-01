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



@app.on_message(filters.command(["المطور"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/e991d85ac3ed77a5bb172.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ [𓏺 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 . 𖠁 ˼](https://t.me/@FH_3B)  ❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @FH_3B ❫
◉ 𝙸𝙳   : ❪ 6274098601 ❫
◉ 𝙱𝙸𝙾  : ❪ -كُن’وحيدآً ولا تكن بِديلآً𓃠.. @FH_3B ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁¹", url=f"https://t.me/FH_3B"),
                ],[
                InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙻𝙸𝙽𝙳𝙰", url=f"https://t.me/KB_HE"), 
                ]
            ]
        ),
    )                                       