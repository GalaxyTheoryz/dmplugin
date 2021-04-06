import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class DMUser(commands.Cog): 
    """DMs a user a message"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def dm(ctx, user_id=None, *, args=None):
     if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")

def setup(bot):
    bot.add_cog(dmuserplugin(bot))
