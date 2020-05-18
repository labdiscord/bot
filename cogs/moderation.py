import discord 
from discord.ext import commands 
from datetime import datetime 

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(aliases=['m'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: discord.Member = None, *, reason = None):
        server = ctx.guild
        if not user:
            return await ctx.send(f"User please.")
        if reason is None:
            reason = "No reason provided."
        if user == ctx.author:
            return await ctx.send(f":rolf: Don't be stupid.")
        if user.top_role.position >= ctx.author.top_role.position and ctx.author != ctx.guild.owner:
            if ctx.author == server.owner:
                pass 
            else:
                return await ctx.send(f"You are unable to mute someone that is higher or equal to your role position.")
        muted = discord.utils.get(server.roles, name="Muted")
        try:
            await user.add_roles(muted, reason=reason)
        except:
            return await ctx.send(f"I am unable to mute that user. Please check my position in the roles and if I have the correct permisisons.")
        await ctx.send(F":ok_hand: Muted.")
        logs = server.get_channel(707464646625591337)
        tm = datetime.utcnow().strftime("%I:%M")
        await logs.send(f"`[{tm}]` :no_mouth: {user.mention} has been muted indefinitely by {ctx.author}.")
        
def setup(bot):
    bot.add_cog(Moderation(bot))
