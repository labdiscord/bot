import discord 
from discord.ext import commands 
from pymongo import MongoClient  as mcl
import asyncio

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="faq")
    async def faq(self,ctx):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return
        desc="""
Welcome to Discord Labs!
The home of **[Usercord](https://usercord.org)**, **[Statcord](https://statcord.com)**, and **[Bots @ Discord Labs](https://bots.discordlabs.org)**!

**So what do you guys do?**
We are building the next generation of Discord Sites And Tools

**What sites have you built?**
You can find a full list over in <#694967215723774072>

**Can I apply to be staff?**
You can check if staff applications are open in <#678408619737481226>.

**Who owns this place?**
<@365958975201738764> and <@651582809776979968>

**I'd like to get my bot certified!**
Open a ticket in <#698422778575192094> and answer the questions asked.

**I have question thats not listed here.**
Thats cool, you can ask it in <#672168369130045440>"""
        
        embed=discord.Embed(title="Discord Labs FAQ",description=desc,color=self.bot.embed)
        embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)



    @commands.command(name="rules")
    async def rules(self,ctx):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return
        desc="""
Before you do anything, we strongly suggest you familirize yourself with the rules and information listed below.

**Website:** [discordlabs.org](https://discordlabs.org)
Bot List: [bots.discordlabs.org](https://bots.discordlabs.org)
Usercord: [usercord.org](https://usercord.org)
Statcord: [statcord.com](https://statcord.com)
        """

        embed=discord.Embed(title="Welcome to Discord Labs!",description=desc,color=self.bot.embed)
        #embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)

        desc="""
    1) Follow the Discord ToS **at all times.**
    2) No NSFW content in this server.
    3) No spamming, advertising or DM'ing unsolicited invites.
    4) Only use bots in <#672180506363822111>, <#672180547744956446> and <#672180644171743232>
    5) No characters that are not easily typable on a Ṷ̶̞S̱ ̢̲̜k͠e̞̬͇y̟͕͝b̻̤͞o̱̹̳a͇͖̕r̤d͍̫́ in your username/nickname.
    6) Channels are to be used for their specific purposes.
    7) **Use Common Sense**
        """

        embed=discord.Embed(title="Lab Rules",description=desc,color=self.bot.embed)
        #embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)

        desc="""
        A list of vanities owned by Discord Labs. To use these vanities, add your bot/your user ID to the end of the URL. Ex. [dbots.cc/stock](https://dbots.cc/stock) redirects to (bots.discordlabs.org/stock)[https://bots.discordlabs.org/stock]
        [usercord](https://usercord.org)
        - [dsc.ninja](https://dsc.ninja)
        - [dusers.best](https://dusers.best)
        - [duser.best](https://duser.best)
        
        [Bots @ Discord Labs](https://bots.discordlabs.org)
        - [dbots.best](https://dbots.best)
        - [dbot.best](https://dbot.best)
        - [discordbots.best](https://discordbots.best)
        - [dlabs.best](https://dlabs.best)
        - [dlabs.cc](https://dlabs.cc)
        - [dbots.cc](https://dbots.cc)
        """
        embed=discord.Embed(title="Lab Vanities",description=desc,color=self.bot.embed)
        #embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)

        desc="""
        [discordlabs.org](https://discordlabs.org) - Main Lab Website
        [bots.discordlabs.org](https://bots.discordlabs.org) - Bot List
        [bots.discordlabs.org](https://bots.discordlabs.org/submit) - Bot Submissions
        [queue.discordlabs.org](https://queue.discordlabs.org) - Bot Queue

        [statcord.com](https://statcord.com) - Grow your Discord Bot, the better way.
        [usercord.org](https://usercord.org) - Stay safe on Discord, use Usercord.
        """

        embed=discord.Embed(title="Lab Links",description=desc,color=self.bot.embed)
        embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)
        
        



        
        



    
        
def setup(bot): 
    bot.add_cog(Update(bot))