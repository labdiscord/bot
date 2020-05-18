
import discord 
from discord.ext import commands 
from datetime import datetime, timedelta 
import re 
import functools

inv = r'discord(\.com|\.gg)[\/invite\/]?(?:(?!.*[Ii10OolL]).[a-zA-Z0-9]{5,6}|[a-zA-Z0-9\-]{2,32})'

class AntiInvite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_message(self, message):
        server = message.guild
        rere = re.compile(inv)
        invites = rere.findall(message.content)
        roles = ["Lab Security Staff"]
        try:
            getter = functools.partial(discord.utils.get, message.author.roles)
            if any(getter(name=item) is not None for item in roles):
                return
        except:
            return
        tm = datetime.utcnow().strftime("%I:%M")
        if invites:
            logs = server.get_channel(707464646625591337)
            await message.delete()
            await message.channel.send(f":ok_hand: No invites please.", delete_after=4)
            await logs.send(f"`[{tm}]` {message.author.mention}'s message has been censored because it contained a Discord invite.")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        server = message.guild 
        tm = datetime.utcnow().strftime("%I:%M")
        logs = server.get_channel(707464646625591337)
        embed = discord.Embed(color=0xf5cb42, timestamp=datetime.now())
        embed.title = "Message Deleted"
        embed.description = f"**Message by {message.author} was deleted in {message.channel.mention}:**\n{message.content}"
        await logs.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            server = after.guild
            logs = server.get_channel(707464646625591337)
            embed = discord.Embed(color=0xf5cb42, timestamp=datetime.now())
            embed.title = "Message Editted"
            embed.add_field(name="Before Content", value=before.content, inline=False)
            embed.add_field(name="After Content", value=after.content, inline=False)
            await logs.send(embed=embed)
            rere = re.compile(inv)
            
            invites = rere.findall(after.content)
            roles = ["Lab Security Staff"]
            try:
                getter = functools.partial(discord.utils.get, after.author.roles)
                if any(getter(name=item) is not None for item in roles):
                    return
            except:
                return
            
            tm = datetime.utcnow().strftime("%I:%M")
            if invites:
                await after.delete()
                await after.channel.send(f":ok_hand: No invites please.", delete_after=4)
                await logs.send(f"`[{tm}]` {after.author.mention}'s message has been censored because it contained a Discord invite.")
        except:
            pass

def setup(bot):
    bot.add_cog(AntiInvite(bot))
