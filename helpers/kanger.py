# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import UserDeactivatedBan
from helpers.forwarder import ForwardMessage


async def Kanger(c: Client, m: Message):
    await m.edit(text=f"Checking `{str(Config.FORWARD_FROM_CHAT_ID[0])}` ...")
    await asyncio.sleep(2)
    try:
        ForwardFromChat = await c.get_chat(chat_id=Config.FORWARD_FROM_CHAT_ID[0])
        await m.edit(text=f"Successfully Linked with `{ForwardFromChat.title}` !")
    except Exception as err:
        await m.edit(text=f"Sorry, can't get **Forward From Chat**!\n\n**Error:** `{err}`")
        return 400
    await asyncio.sleep(2)
    for i in range(len(Config.FORWARD_TO_CHAT_ID)):
        await m.edit(text=f"Checking `{Config.FORWARD_TO_CHAT_ID[i]}` ...")
        await asyncio.sleep(2)
        try:
            ForwardToChat = await c.get_chat_member(chat_id=Config.FORWARD_TO_CHAT_ID[i], user_id=(await c.get_me()).id)
            if ForwardToChat.can_send_messages is False:
                await m.edit(text=f"Sorry, you don't have permission to send messages in {ForwardToChat.title} !")
                return 400
            await m.edit(text=f"Successfully Linked with `{ForwardToChat.title}` !")
            await asyncio.sleep(2)
        except Exception as err:
            await m.edit(text=f"Sorry, can't get **Forward To Chat**!\n\n**Error:** `{err}`")
            return 400
    await asyncio.sleep(2)
    await m.edit(text="Trying to Forward Now ...")
    async for message in c.iter_history(chat_id=Config.FORWARD_FROM_CHAT_ID[0], reverse=True):
        await asyncio.sleep(Config.SLEEP_TIME)
        try:
            try_forward = await ForwardMessage(c, message)
            if try_forward == 400:
                return 400
        except UserDeactivatedBan:
            print("Congratulations!\nYour Account Banned Successfully!\nI already told you use a Fake Account. Hope you remember.")
            break
        except Exception as err:
            await c.send_message(chat_id="me", text=f"#ERROR: `{err}`")
    await m.edit(text="Channel Files Successfully Kanged!\n\n©️ A Forwarder Userbot by @AbirHasan2005")
