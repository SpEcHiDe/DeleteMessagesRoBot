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
from bot import (
    AKTIFPERINTAH,
    BEGINNING_SEL_DEL_MESSAGE,
    DEL_FROM_COMMAND,
    DEL_TO_COMMAND,
    IN_CORRECT_PERMISSIONS_MESSAGE,
    NOT_USED_DEL_FROM_DEL_TO_MESSAGE,
    SEL_DEL_COMMAND
)
from bot.bot import Bot
from bot.helpers.custom_filter import allowed_chat_filter
from bot.helpers.make_user_join_chat import make_chat_user_join
from bot.helpers.get_messages import get_messages


@Bot.on_message(
    filters.command(SEL_DEL_COMMAND) &
    allowed_chat_filter
)
async def del_selective_command_fn(client: Bot, message: Message):
    status_message = await message.reply_text(BEGINNING_SEL_DEL_MESSAGE)

    s__, nop = await make_chat_user_join(
        client.USER,
        client.USER_ID,
        message
    )
    if not s__:
        await status_message.edit_text(
            IN_CORRECT_PERMISSIONS_MESSAGE.format(
                nop
            ),
            disable_web_page_preview=True
        )
        return

    current_selections = AKTIFPERINTAH.get(message.chat.id)
    if not current_selections:
        await status_message.edit(NOT_USED_DEL_FROM_DEL_TO_MESSAGE)
        return

    flt_type = []
    if len(message.command) > 1:
        flt_type = message.command[1:]

    await get_messages(
        client.USER,
        message.chat.id,
        current_selections.get(DEL_FROM_COMMAND),
        current_selections.get(DEL_TO_COMMAND),
        flt_type
    )
    try:
        await status_message.delete()
        await message.delete()
    except:
        pass
    del AKTIFPERINTAH[message.chat.id]

    # leave the chat, after task is done
    await client.USER.leave_chat(message.chat.id)
    await client.leave_chat(message.chat.id)
