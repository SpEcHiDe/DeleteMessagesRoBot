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

from typing import List
from bot import (
    TG_MAX_SEL_MESG,
    TG_MIN_SEL_MESG
)
from bot.bot import Bot
from bot.helpers.delete_messages import mass_delete_messages


async def get_messages(
    client: Bot,
    chat_id: int,
    min_message_id: int,
    max_message_id: int,
    filter_type_s: List[str]
):
    messages_to_delete = []
    async for msg in client.iter_history(
        chat_id=chat_id,
        limit=None
    ):
        if (
            min_message_id <= msg.message_id and
            max_message_id >= msg.message_id
        ):
            if len(filter_type_s) > 0:
                for filter_type in filter_type_s:
                    obj = getattr(msg, filter_type)
                    if obj:
                        messages_to_delete.append(msg.message_id)
            else:
                messages_to_delete.append(msg.message_id)
        # append to the list, based on the condition
        if len(messages_to_delete) > TG_MAX_SEL_MESG:
            await mass_delete_messages(
                client,
                chat_id,
                messages_to_delete
            )
            messages_to_delete = []
    # i don't know if there's a better way to delete messages
    if len(messages_to_delete) > TG_MIN_SEL_MESG:
        await mass_delete_messages(
            client,
            chat_id,
            messages_to_delete
        )
        messages_to_delete = []
