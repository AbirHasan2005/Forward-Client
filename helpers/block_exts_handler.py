# (c) @AbirHasan2005

from configs import Config
from pyrogram.types import Message


async def CheckBlockedExt(event: Message):
    media = event.document or event.video or event.audio or event.animation
    if (Config.BLOCK_FILES_WITHOUT_EXTENSIONS is True) and ("." not in media.file_name):
        return True
    if (media is not None) and (media.file_name is not None):
        _file = media.file_name.rsplit(".", 1)
        if len(_file) == 2:
            if (_file[-1].lower() in Config.BLOCKED_EXTENSIONS) or (_file[-1].upper() in Config.BLOCKED_EXTENSIONS):
                return True
            else:
                return False
        else:
            return False
