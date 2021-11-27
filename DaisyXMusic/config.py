# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("AQCAuw_kA5flpzuT5IG3bh9j0MWxSZUDxud7StDNEaHqw1DiY_QizRAS3rfXzk06gEpxroQUlKRJBN35O2156QBMlnpPEGVfBQzdD6nPjF8FUzkorZfArNlNSxKKzbJXtr7T-thirHBU6MqfZ5P3mgv9OKJHZbElXuutrXgQLmYNdjHWukMRJ2w8PP2QI1PPbrYN_4p-e7W6H8EBMsMJibvswr0coy_04Ys5NbYAB5sf7xCNtzl-5xU7yEyXIpJAvpVBde2OeL1e9oyPYaRE8bCJYbLnrrhNg2Vj5iYg8zwv4iOxOPdkD-FQGaLoXYSFKVfLDUcdxeG65qDZvvn_qNcIdw8lGAA", "session")
BOT_TOKEN = getenv("2133263281:AAErmTPq52mQTSQy0W5KH93eZyXqMrM3lc8")
BOT_NAME = getenv("LosSantosRobot")
UPDATES_CHANNEL = getenv("truewildthoughts", "DaisyXupdates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("8650591", ""))
API_HASH = getenv("4a097e5213b9ebff472a0212af38e3a7")
BOT_USERNAME = getenv("LosSantosRobot")
ASSISTANT_NAME = getenv("LosSantosAssistant", "DaisyXhelper")
SUPPORT_GROUP = getenv("International_chatting_Legends", "DaisySupport_Official")
PROJECT_NAME = getenv("RadioLosSantos", "DaisyXMusic v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("900", "7"))
ARQ_API_KEY = getenv("DFVBYC-QSLUWT-YUPNPQ-GTUZDK-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("-1001642145931", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("2037030571").split()))
