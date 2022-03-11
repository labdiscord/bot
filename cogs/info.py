import discord 
from discord.ext import commands 
from pymongo import MongoClient  as mcl
import asyncio

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="faq")
    @commands.has_role(608714147378626570)
    async def faq(self,ctx):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return

        desc="""
Below we have a list of the common issues you might run into! Take the time to **READ** them as most all questions are answered right here. \n\nIf your question is still not answered, feel free to ask in <#695065137698045993> or open a <#728695849286107288>.
        """
        embed1=discord.Embed(title="➤ Discord Labs FAQ",description=desc,color=0xFF0000)
        embed2=discord.Embed(title="➤ How do I become certified?",description="Checkout <#698422778575192094>. If you can't see that channel, wait until you have the <@&672176587449565233> role.",color=self.bot.embed)
        embed2=discord.Embed(title="➤ When will my bot get approved?",description="**We do not know.** \nJust view your bot on our live [queue](https://queue.discordlabs.org) which can be accessed by visiting [bots.discordlabs.org/queue](https://bots.discordlabs.org/queue). \n\n**Do not** under any circumstance ask for approvers to approve your bot / the status of your application, **we will get to your bot when we have time.**",color=0xFFA500)
        embed3=discord.Embed(title="➤ I want to be staff!",description="Thats amazing! We'll be happy to faciliate that, just join our applications discord at [discord.gg/wbgEJGb](https://discord.gg/wbgEJGb). \n\nKeep in mind that we only select approvers when we need them so don't be suprised if you don't get a response right away, it may take a few months!",color=0xFFFF00)
        embed4=discord.Embed(title="➤ My Statcord won't work :(",description="That's not a problem! We're here to help. If its a general implementation ask in <#695065137698045993>, otherwise open a <#695065137698045993>.",color=0x008000)
        embed5=discord.Embed(title="➤ I've found a bug / have a suggestion.",description="Report any bugs in <#695034845046505552> and post suggestions by typing `-suggest [your suggestion]` in <#760468980154105888>.\n\n**If you find a critical bug please open a <#728695849286107288>.**",color=self.bot.embed)
        #embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        #await ctx.send(embed=embed)

        avatar = await ctx.guild.icon_url.read()
        webhook = await ctx.channel.create_webhook(name="Discord Labs",avatar=avatar, reason="Do I need one?")
        await webhook.send(embeds=[embed1,embed2,embed3,embed4,embed5])



    @commands.command(name="bots")
    @commands.has_role(608714147378626570)
    async def bots(self,ctx):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return

        desc="""
Below we have a list of the common issues you might run into! Take the time to **READ** them as most all questions are answered right here. \n\nIf your question is still not answered, feel free to ask in <#695065137698045993> or open a <#728695849286107288>.
        """        
        embed1=discord.Embed(title="➤ Discord Labs FAQ",description=desc,color=0xFF0000)
        embed2=discord.Embed(title="➤ How do I become certified?",description="Checkout <#698422778575192094>. If you can't see that channel, wait until you have the <@&672176587449565233> role.",color=self.bot.embed)
        embed2=discord.Embed(title="➤ When will my bot get approved?",description="**We do not know.** \nJust view your bot on our live [queue](https://queue.discordlabs.org) which can be accessed by visiting [bots.discordlabs.org/queue](https://bots.discordlabs.org/queue). \n\n**Do not** under any circumstance ask for approvers to approve your bot / the status of your application, **we will get to your bot when we have time.**",color=0xFFA500)
        embed3=discord.Embed(title="➤ I want to be staff!",description="Thats amazing! We'll be happy to faciliate that, just join our applications discord at [discord.gg/wbgEJGb](https://discord.gg/wbgEJGb). \n\nKeep in mind that we only select approvers when we need them so don't be suprised if you don't get a response right away, it may take a few months!",color=0xFFFF00)
        embed4=discord.Embed(title="➤ My Statcord won't work :(",description="That's not a problem! We're here to help. If its a general implementation ask in <#695065137698045993>, otherwise open a <#695065137698045993>.",color=0x008000)
        embed5=discord.Embed(title="➤ I've found a bug / have a suggestion.",description="Report any bugs in <#695034845046505552> and post suggestions by typing `-suggest [your suggestion]` in <#760468980154105888>.\n\n**If you find a critical bug please open a <#728695849286107288>.**",color=self.bot.embed)
        #embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        #await ctx.send(embed=embed)

        avatar = await ctx.guild.icon_url.read()
        webhook = await ctx.channel.create_webhook(name="Discord Labs",avatar=avatar, reason="Do I need one?")
        await webhook.send(embeds=[embed1,embed2,embed3,embed4,embed5])



    @commands.command(name="rules")
    @commands.has_role(608714147378626570)
    async def rules(self,ctx):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return
        desc="""
Before you do anything, we strongly suggest you familiarize yourself with the rules and information listed below.

**Website:** [discordlabs.org](https://discordlabs.org)
Bot List: [bots.discordlabs.org](https://bots.discordlabs.org)
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
    7) Don't ping staff (Excluding <@651582809776979968>, ping him all u want)
    7) **Use Common Sense**
        """

        embed=discord.Embed(title="Lab Rules",description=desc,color=self.bot.embed)
        #embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)

        desc="""
        A list of vanities owned by Discord Labs. To use these vanities, add your bot/your user ID to the end of the URL. Ex. [dbots.cc/stock](https://dbots.cc/stock) redirects to [bots.discordlabs.org/stock](https://bots.discordlabs.org/stock)
       
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
        """

        embed=discord.Embed(title="Lab Links",description=desc,color=self.bot.embed)
        embed.set_footer(text='© 2020 Discord Labs',icon_url=ctx.channel.guild.icon_url)
        await ctx.send(embed=embed)
        
        



        
        



    
        
def setup(bot): 
    bot.add_cog(Update(bot))
