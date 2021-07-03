# (c) @AbirHasan2005

from pyrogram.types import Message
from configs import Config


async def CheckFileSize(msg: Message):
    media = msg.video or msg.document or msg.audio or msg.photo or msg.animation
    if (Config.MINIMUM_FILE_SIZE is not None) and (media.file_size < int(Config.MINIMUM_FILE_SIZE)):
        return False
    else:
        return True
