# (c) @AbirHasan2005
# This is Telegram Messages Forwarder UserBot!

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from configs import Config

User = Client(session_name=Config.STRING_SESSION, api_hash=Config.API_HASH, api_id=Config.API_ID)


@User.on_message(filters.text | filters.media & ~filters.edited)
async def main(client, message):
    # Checks
    if not Config.FORWARD_TO_CHAT_ID or not Config.FORWARD_FROM_CHAT_ID or not Config.USER_ID:
        await client.send_message(chat_id="me",
                                  text=f"#VARS_MISSING: Please Set `FORWARD_FROM_CHAT_ID` & `FORWARD_TO_CHAT_ID` & `USER_ID` Config!")
        return

    if message.text == "!start" and message.from_user.id == int(Config.USER_ID):
        await message.edit(text="Hi, Myself!\nI am Alive XD", parse_mode="Markdown", disable_web_page_preview=True)
    elif message.text == "!help" and message.from_user.id == int(Config.USER_ID):
        await message.edit(
            text="This UserBot can forward messages from any Chat to any other Chat XD\n\nDeveloper: @AbirHasan2005",
            parse_mode="Markdown", disable_web_page_preview=True)
    elif message.chat.id == (int(Config.FORWARD_FROM_CHAT_ID)):
        try:
            await message.forward(int(Config.FORWARD_TO_CHAT_ID))
        except FloodWait as e:
            await client.send_message(chat_id="me", text=f"#FloodWait: Stopping Forwarder for `{e.x}s`!")
            await asyncio.sleep(e.x)
        except Exception as err:
            await client.send_message(chat_id="me", text=f"#ERROR: `{err}`")


User.run()
