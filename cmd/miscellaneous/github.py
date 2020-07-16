"""Contains the github command"""

import json
import botutils
from discord.ext import commands
from ._miscellaneous import Miscellaneous

with open('botutils/bot_text.json') as json_file: 
    language = json.load(json_file)

github_str = language["cmd"]["github"]


class Github(Miscellaneous, name = "༺ 𝕸𝖎𝖘𝖈𝖊𝖑𝖑𝖆𝖓𝖊𝖔𝖚𝖘 ༻"):

    @commands.command(
        pass_context=True, 
        name = "github", 
        aliases = ["git"],
        brief = language["doc"]["github"]["brief"],
        help = language["doc"]["github"]["help"],
        description = language["doc"]["github"]["description"]
    )
    @commands.check(botutils.check_if_lobby_or_dm_or_admin)
    async def github(self, ctx):
        await ctx.send(github_str)
