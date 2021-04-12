# (c) @AbirHasan2005 | Thomas Shelby
# This is Telegram Messages Forwarder UserBot!
# Use this at your own risk. I will not be responsible for any kind of issue while using this!

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserDeactivatedBan
from configs import Config

User = Client(session_name=Config.STRING_SESSION, api_hash=Config.API_HASH, api_id=Config.API_ID)


async kanger(msg):
    await msg.edit(text="Forwarding Now ...")
    async for message in User.iter_history(chat_id=int(Config.FORWARD_FROM_CHAT_ID), reverse=True):
        try:
            await message.copy(int(Config.FORWARD_TO_CHAT_ID))
        except FloodWait as e:
            await User.send_message(chat_id="me", text=f"#FloodWait: Stopping Forwarder for `{e.x}s`!")
            await asyncio.sleep(e.x)
        except UserDeactivatedBan:
            print("Congratulations!\nYour Account Banned Successfully!\nI already told you use a Fake Account. Hope you remember.")
            break
        except Exception as err:
            await User.send_message(chat_id="me", text=f"#ERROR: `{err}`")
    await msg.edit(text="Channel Files Successfully Kanged!\n\n©️ A Forwarder Userbot by @AbirHasan2005")


@User.on_message((filters.text | filters.media) & ~filters.edited)
async def main(client, message):
    # Checks
    if (Config.FORWARD_TO_CHAT_ID and Config.FORWARD_FROM_CHAT_ID and Config.USER_ID) is None:
        try:
            await client.send_message(chat_id="me",
                                      text=f"#VARS_MISSING: Please Set `FORWARD_FROM_CHAT_ID` & `FORWARD_TO_CHAT_ID` & `USER_ID` Config!")
        except FloodWait as e:
            await asyncio.sleep(e.x)
        return

    if message.text == "!start" and (message.from_user.id == int(Config.USER_ID)):
        await message.edit(text="Hi, Myself!\nThis is a Forwarder Userbot by @AbirHasan2005", parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == "!help" and (message.from_user.id == int(Config.USER_ID)):
        await message.edit(
            text="This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.\n\n👨🏻‍💻 **Commands:**\n• `!start`\n• `!help`\n• `!kang`\n\n©️ **Developer:** @AbirHasan2005\n👥 **Support Group:** [【★ʟя★】](https://t.me/linux_repo)",
            parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == "!kang" and (message.from_user.id == int(Config.USER_ID)):
        editable = await message.edit(
            text=f"Trying to Get All Messages from `{str(Config.FORWARD_FROM_CHAT_ID)}` and Forwarding to `{str(Config.FORWARD_TO_CHAT_ID)}` ...",
            parse_mode="Markdown", disable_web_page_preview=True)
        await asyncio.sleep(5)
        await kanger(editable)
    elif message.chat.id == (int(Config.FORWARD_FROM_CHAT_ID)):
        try:
            await message.forward(int(Config.FORWARD_TO_CHAT_ID))
        except FloodWait as e:
            await client.send_message(chat_id="me", text=f"#FloodWait: Stopping Forwarder for `{e.x}s`!")
            await asyncio.sleep(e.x)
        except Exception as err:
            await client.send_message(chat_id="me", text=f"#ERROR: `{err}`")


User.run()
