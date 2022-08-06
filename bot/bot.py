#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" MtProto Bot """

from pyrogram import (
    Client,
    __version__
)
from pyrogram.enums import ParseMode
from . import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_SESSION,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
    TG_SLEEP_THRESHOLD
)
from .user import User


class Bot(Client):
    """ modded client for MessageDeletERoBot """
    BOT_ID: int = None
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name=TG_BOT_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "bot.plugins",
                "exclude": [
                    "oatc"
                ]
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
            sleep_threshold=TG_SLEEP_THRESHOLD,
            parse_mode=ParseMode.HTML
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.BOT_ID = usr_bot_me.id
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        self.USER, self.USER_ID = await User().start()
        # hack to get the entities in-memory
        await self.USER.send_message(
            usr_bot_me.username,
            "join https://t.me/SpEcHlDe/857"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
