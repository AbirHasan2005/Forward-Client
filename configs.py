# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(2992000)
    API_HASH = "235b12e862d71234ea222082052822fd"
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = "BAAq1qNpvBphR_DZac-QA8xGRIgDvAcUjSCxUFCMFamMtkTaSg7dMzmdaafkvY23lnmCcE5kPvI0wkgagEDHr1HVhxogIgJCyZCSG7whaHXqZ3fSqUY3Y6c92HeOkvKChosLv77xFynbfzghgeX3siDcLL5B3v8ENDrmdww5HmdNQqRGBDTJ_GS2-YkciKlsFvW6aXXSR75FVc_vs8K8FcAo6e_SlW2tusB8rit8iBXgGxWwPsSZqJvsJ4tl8K0Uj9a83LPTb4ti8_cX0mv0gd4-voX5omGmfPfk952tYsu_CKj5VCowSdVRIcG77Qwq38R5zKDzBdpeJiaWs5HH2Yf_AAAAAVRaCsYA"
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = []
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = []
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(3)
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
