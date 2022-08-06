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

from pyrogram.types import Message
from pyrogram.enums import MessageEntityType
from .delall_bot_links import extract_c_m_ids


def knemblook(
    message: Message
):
    _store_r = {}
    entities = (
        message.entities or
        message.caption_entities or
        []
    )
    text = (
        message.text or
        message.caption or
        ""
    )
    if message and text and len(entities) > 0:
        for one_entity in entities:
            _url = None
            if one_entity.type == MessageEntityType.URL:
                _url = text[
                    one_entity.offset:one_entity.offset + one_entity.length
                ]
            elif one_entity.type == MessageEntityType.TEXT_LINK:
                _url = one_entity.url
            if _url:
                chat_id, message_id = extract_c_m_ids(_url)
                if chat_id not in _store_r:
                    _store_r[chat_id] = []
                _store_r[chat_id].append(message_id)
    return _store_r
