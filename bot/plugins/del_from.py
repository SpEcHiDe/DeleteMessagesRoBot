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

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import (
    ChatAdminRequired
)
from bot import (
    AKTIFPERINTAH,
    DEL_FROM_COMMAND
)
from bot.bot import Bot
from bot.helpers.custom_filter import allowed_chat_filter


@Bot.on_message(
    filters.command(DEL_FROM_COMMAND) &
    filters.reply &
    allowed_chat_filter
)
async def del_from_command_fn(client: Bot, message: Message):
    try:
        status_message = await message.reply_text(
            "trying to save starting message_id"
        )
    except ChatAdminRequired:
        status_message = None
    if message.chat.id not in AKTIFPERINTAH:
        AKTIFPERINTAH[message.chat.id] = {}
    AKTIFPERINTAH[
        message.chat.id
    ][
        DEL_FROM_COMMAND
    ] = message.reply_to_message.id
    if status_message:
        await status_message.edit_text(
            "saved starting message_id. "
            "https://github.com/SpEcHiDe/DeleteMessagesRoBot"
        )
        await status_message.delete()
    await message.delete()
