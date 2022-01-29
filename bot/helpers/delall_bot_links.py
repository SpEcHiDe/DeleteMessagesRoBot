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

from typing import Tuple, Union


def extract_c_m_ids(message_link: str) -> Tuple[Union[str, int], int]:
    p_m_link = message_link.split("/")
    chat_id, message_id = None, None
    if len(p_m_link) == 6:
        # private link
        if p_m_link[3] == "c":
            # the Telegram private link
            chat_id, message_id = int("-100" + p_m_link[4]), int(p_m_link[5])
        elif p_m_link[3] == "DMCATelegramBot":
            # bleck magick
            chat_id, message_id = int(p_m_link[4]), int(p_m_link[5])
    elif len(p_m_link) == 5:
        # public link
        chat_id, message_id = str("@" + p_m_link[3]), int(p_m_link[4])
    return chat_id, message_id
