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
    BEGINNING_DEL_ALL_MESSAGE,
    THANK_YOU_MESSAGE,
    IN_CORRECT_PERMISSIONS_MESSAGE,
    SHTL_BOT_HCAT_QO,
    SHTL_USR_HCAT_QO
)
from bot.bot import Bot
from bot.helpers.gulmnek import knemblook
from bot.helpers.delete_messages import mass_delete_messages
from bot.helpers.help_for_14121 import check_perm
from bot.helpers.make_user_join_chat import make_chat_user_join


@Bot.on_message(
    filters.incoming &
    filters.create(
        lambda _, __, msg: (
            msg and
            msg.chat and
            msg.from_user and
            # we don't want to deal with
            # Telegram weirdness for now
            msg.chat.type == "private" and
            msg.forward_from and
            msg.forward_from.id == 454000
        ),
        "Incoming454000Messages"
    )
)
async def dmca_spec_del_nf(client: Bot, message: Message):
    bot_id = await client.get_me()
    status_message = await message.reply_text(
        BEGINNING_DEL_ALL_MESSAGE,
        quote=True
    )
    all_id_stores_ = knemblook(message)
    for chat_id in all_id_stores_:
        # 1) check bot permissions in chat_id
        aqo = check_perm(client, chat_id, message.from_user.id)
        if not aqo:
            continue
        qbo = check_perm(client, chat_id, bot_id)
        if not qbo:
            await status_message.reply_text(
                IN_CORRECT_PERMISSIONS_MESSAGE,
                quote=True
            )
            continue
        heck_mesg = await client.get_messages(
            chat_id,
            all_id_stores_[chat_id][0],
            replies=0
        )
        # 2) make user join chat
        await make_chat_user_join(
            client,
            client.USER_ID,
            heck_mesg
        )

        # 3) delete the list of messages
        await mass_delete_messages(
            client.USER,
            chat_id,
            all_id_stores_[chat_id]
        )

        # 4) leave chat
        # leave the chat, after task is done
        if SHTL_USR_HCAT_QO:
            await client.USER.leave_chat(chat_id)
        if SHTL_BOT_HCAT_QO:
            await client.leave_chat(chat_id)

    await status_message.edit_text(
        THANK_YOU_MESSAGE
    )
