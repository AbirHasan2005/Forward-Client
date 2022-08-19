# (c) @AbirHasan2005 | Thomas Shelby
# This is Telegram Messages Forwarder UserBot!
# Use this at your own risk. I will not be responsible for any kind of issue while using this!

import os
import sys
import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from configs import Config
from helpers.kanger import Kanger
from helpers.forwarder import ForwardMessage

RUN = {"isRunning": True}
User = Client(
    name='pyrogram',
    api_hash=Config.API_HASH,
    api_id=Config.API_ID,
    in_memory=True,
    session_string=Config.STRING_SESSION
)


@User.on_message((filters.text | filters.media))
async def main(client: Client, message: Message):
    if (-100 in Config.FORWARD_TO_CHAT_ID) or (-100 in Config.FORWARD_FROM_CHAT_ID):
        try:
            await client.send_message(chat_id="me",
                                      text=f"#VARS_MISSING: Please Set `FORWARD_FROM_CHAT_ID` or `FORWARD_TO_CHAT_ID` Config!")
        except FloodWait as e:
            await asyncio.sleep(e.value)
        return
    if (message.text == "!start") and message.from_user.is_self:
        if not RUN["isRunning"]:
            RUN["isRunning"] = True
        await message.edit(text=f"Hi, **{(await client.get_me()).first_name}**!\nThis is a Forwarder Userbot by @AbirHasan2005", parse_mode="Markdown",
                           disable_web_page_preview=True)
    elif (message.text == "!stop") and message.from_user.is_self:
        RUN["isRunning"] = False
        return await message.edit("Userbot Stopped!\n\nSend `!start` to start userbot again.")
    elif (message.text == "!help") and message.from_user.is_self and RUN["isRunning"]:
        await message.edit(
            text=Config.HELP_TEXT,
            parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text and (message.text.startswith("!add_forward_")) and message.from_user.is_self and RUN["isRunning"]:
        if len(message.text.split(" ", 1)) < 2:
            return await message.edit(f"{message.text} chat_id")
        for x in message.text.split(" ", 1)[-1].split(" "):
            if x.isdigit() and message.text.startswith("!add_forward_to_chat"):
                Config.FORWARD_TO_CHAT_ID.append(int(x))
            elif x.isdigit() and message.text.startswith("!add_forward_from_chat"):
                Config.FORWARD_FROM_CHAT_ID.append(int(x))
            else:
                pass
    elif message.text and (message.text.startswith("!remove_forward_")) and message.from_user.is_self and RUN["isRunning"]:
        if len(message.text.split(" ", 1)) < 2:
            return await message.edit(f"{message.text} chat_id")
        for x in message.text.split(" ", 1)[-1].split(" "):
            if x.isdigit() and message.text.startswith("!remove_forward_to_chat"):
                Config.FORWARD_TO_CHAT_ID.remove(int(x))
            elif x.isdigit() and message.text.startswith("!remove_forward_from_chat"):
                Config.FORWARD_FROM_CHAT_ID.remove(int(x))
            else:
                pass
    elif (message.text in ["!restart"]) and message.from_user.is_self:
        if Config.HEROKU_APP is None:
            await message.edit(
                text="Restarting Userbot ...",
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
            # https://stackoverflow.com/a/57032597/15215201
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            await message.edit(
                text="Restarting Heroku Dyno ..."
            )
            Config.HEROKU_APP.restart()
            time.sleep(30)
    elif (message.text == "!kang") and message.from_user.is_self and RUN["isRunning"]:
        if len(Config.FORWARD_FROM_CHAT_ID) > 1:
            await message.edit(
                text="Sorry Sir,\nWe can Kang only one Chat! But you put multiple Chat IDs in `FORWARD_FROM_CHAT_ID` Config!",
                disable_web_page_preview=True
            )
            return
        await message.edit(
            text=f"Trying to Get All Messages from `{str(Config.FORWARD_FROM_CHAT_ID[0])}` and Forwarding to {' '.join(str(Config.FORWARD_TO_CHAT_ID))} ...",
            parse_mode="Markdown", disable_web_page_preview=True)
        await asyncio.sleep(5)
        try_kang = await Kanger(c=User, m=message)
        if try_kang == 400:
            return
    elif message.chat.id in Config.FORWARD_FROM_CHAT_ID and RUN["isRunning"]:
        try_forward = await ForwardMessage(client, message)
        if try_forward == 400:
            return


User.run()
