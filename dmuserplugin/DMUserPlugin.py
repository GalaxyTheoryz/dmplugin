import discord
from discord.ext import commands

class DMUserPlugin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)
    
    @commands.command(aliases=['dmu'])
    @checks.has_permissions(manage_messages=True)
    async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")

    @commands.Cog.listener()
    async def on_ready(self):
        async with self.bot.session.post("https://counter.modmail-plugins.ionadev.ml/api/instances/announcement", json={'id': self.bot.user.id}):
            print("Posted to Plugin API")




def setup(bot):
    bot.add_cog(DMUserPlugin(bot))