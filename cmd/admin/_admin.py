"""Contains admins only commands"""

import traceback
import json
import botutils
from discord.ext import commands

with open('botutils/bot_text.json') as json_file: 
    language = json.load(json_file)

user_not_found_str = language["errors"]["user_not_found"]
missing_user_str = language["errors"]["missing_user"]
error_str = language["system"]["error"]


class Admin(commands.Cog, name = "༺ 𝕬𝖉𝖒𝖎𝖓𝖎𝖘𝖙𝖗𝖆𝖙𝖔𝖗 ༻"):
    """Admins only commands cog"""
    
    def __init__(self, client):
        self.client = client

    def cog_check(self, ctx):
        return botutils.check_if_admin(ctx)

    async def cog_command_error(self, ctx, error):
        """Error handling on command"""

        # Case: bad argument (user not found)
        if isinstance(error, commands.BadArgument):
            await ctx.send(user_not_found_str.format(ctx.author.mention))
            return
        # Case: missing required argument (user not specified)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(missing_user_str.format(ctx.author.mention))
            return
        elif isinstance(error, commands.CheckFailure):
            return
        else:
            try:
                raise error
            except Exception:
                await ctx.send(error_str)
                await botutils.log(botutils.Level.error, traceback.format_exc()) 