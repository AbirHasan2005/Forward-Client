# (c) @AbirHasan2005

from configs import Config
from pyrogram.types import Message


async def FilterMessage(message: Message):
    if (message.forward_from or message.forward_from_chat) and ("forwarded" not in Config.FORWARD_FILTERS):
        return 400
    if (len(Config.FORWARD_FILTERS) == 9) or ((message.video and ("video" in Config.FORWARD_FILTERS)) or (message.document and ("document" in Config.FORWARD_FILTERS)) or (message.photo and ("photo" in Config.FORWARD_FILTERS)) or (message.audio and ("audio" in Config.FORWARD_FILTERS)) or (message.text and ("text" in Config.FORWARD_FILTERS)) or (message.animation and ("gif" in Config.FORWARD_FILTERS)) or (message.poll and ("poll" in Config.FORWARD_FILTERS)) or (message.sticker and ("sticker" in Config.FORWARD_FILTERS))):
        return 200
    else:
        return 400
