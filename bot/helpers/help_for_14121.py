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

from pyrogram.errors import (
    UserNotParticipant
)
from bot.bot import Bot


async def check_perm(client: Bot, chat_id: int, user_id: int) -> bool:
    try:
        _a_ = await client.get_chat_member(
            chat_id,
            user_id
        )
    except UserNotParticipant:
        return False
    else:
        if _a_.can_delete_messages:
            return True
        else:
            return False
