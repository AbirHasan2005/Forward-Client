# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from helpers.filters import FilterMessage
from helpers.file_size_checker import CheckFileSize
from helpers.block_exts_handler import CheckBlockedExt


async def ForwardMessage(client: Client, msg: Message):
    try:
        ## --- Check 1 --- ##
        can_forward = await FilterMessage(message=msg)
        if can_forward == 400:
            return 400
        ## --- Check 2 --- ##
        has_blocked_ext = await CheckBlockedExt(event=msg)
        if has_blocked_ext is True:
            return 400
        ## --- Check 3 --- ##
        file_size_passed = await CheckFileSize(msg=msg)
        if file_size_passed is False:
            return 400
        ## --- Check 4 --- ##
        for i in range(len(Config.FORWARD_TO_CHAT_ID)):
            try:
                if Config.FORWARD_AS_COPY is True:
                    await msg.copy(Config.FORWARD_TO_CHAT_ID[i])
                else:
                    await msg.forward(Config.FORWARD_TO_CHAT_ID[i])
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await client.send_message(chat_id="me", text=f"#FloodWait: Stopped Forwarder for `{e.value}s`!")
                await asyncio.sleep(Config.SLEEP_TIME)
                await ForwardMessage(client, msg)
            except Exception as err:
                await client.send_message(chat_id="me", text=f"#ERROR: `{err}`\n\nUnable to Forward Message to `{str(Config.FORWARD_TO_CHAT_ID[i])}`")
    except Exception as err:
        await client.send_message(chat_id="me", text=f"#ERROR: `{err}`")
