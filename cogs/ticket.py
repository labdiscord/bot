import discord 
from discord.ext import commands 
from pymongo import MongoClient  as mcl
import asyncio

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="apply")
    async def apply(self,ctx):
        if (not ctx.guild or ctx.guild.id!=753089953256308957):
            embed=discord.Embed(title="Wrong Servers.",description=F"{ctx.author.mention}, this server can't be used to start an application. Use the [Application Server](https://discord.gg/wbgEJGb).",color=0xFF0000)
            await ctx.send(embed=embed,delete_after=10)
            await asyncio.sleep(10)
            return await ctx.message.delete()

        if(ctx.channel.id!=754825766885130352):
            embed=discord.Embed(title="Wrong Channel.",description=F"{ctx.author.mention}, this channel can't be used to start an application. Use <#754825766885130352>.",color=0xFF0000)
            await ctx.send(embed=embed,delete_after=10)
            await asyncio.sleep(10)
            return await ctx.message.delete()
        

        
        guild=ctx.guild
        zuser=ctx.author
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True,send_messages=True),
            ctx.author: discord.PermissionOverwrite(read_messages=True,send_messages=True)
        }
        
        name="ticket-"+str(zuser.name)
        name.replace(" ", "-")
        channel = await guild.create_text_channel(name,overwrites=overwrites,category=self.bot.get_channel(753093653957967993))

        embed=discord.Embed(title="Applications Created!",description=F"{ctx.author.mention}, your applications has been created in {channel.mention}",color=self.bot.embed)
        await ctx.channel.send(embed=embed,delete_after=10)
        await ctx.message.delete()
        await channel.send(content=ctx.author.mention,delete_after=1)
        embed=discord.Embed(title="Application",description=F"Loading...Please wait, this should only take a few seconds.",color=self.bot.embed)
        msg=await channel.send(embed=embed)
        approver="\U0001f1e6"
        moderator="\U0001f1e7"
        support="\U0001f1e8"
        delete="\U0000274c"

        await msg.add_reaction("\U0001f1e6")
        #await msg.add_reaction("\U0001f1e7")
        #await msg.add_reaction("\U0001f1e8")
        await msg.add_reaction("\U0000274c")

        embed=discord.Embed(title="Application",description="**Select The Job You Are Applying For**\n\n:regional_indicator_a: `Bot Approver`\n:x:`Close This Application`",color=self.bot.embed)
        await msg.edit(embed=embed)

        def reactioncheck(reaction,user):
            if (not user.bot):
                if reaction.message.id==msg.id:
                    if reaction.emoji in ["\U0001f1e6","\U0000274c"]:
                        return True
            return False

        reaction, user = await self.bot.wait_for("reaction_add", check=reactioncheck)
        await msg.clear_reactions()

        if reaction.emoji==delete:
            await channel.send("Closing in 5 seconds")
            await asyncio.sleep(5)
            return await channel.delete()
        
        if reaction.emoji==support:
            def check(m):
                return (m.channel == channel and m.author==ctx.author)

            embed=discord.Embed(title="Application: Support Staff",description=F"Allright, lets get started, what is your **First Name?**",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            first=res.content


            embed=discord.Embed(title="Application: Support Staff",description=F"Nice to meet you, {first}. What is the **First** letter of your **Last Name?**",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            last=res.content

            embed=discord.Embed(title="Application: Support Staff",description=F"Awesome, below we have listed several questions, reply with what you think the answer is. **First Question: ** What is the link to the official Discord Labs website?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q1=res.content

            embed=discord.Embed(title="Application: Support Staff",description=F"**Second Question: ** Provide a link to each service provided by Discord Labs and a brief description of each one.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q2=res.content

            embed=discord.Embed(title="Application: Support Staff",description=F"**Third Question: ** What are all the Vanity URL's owned by Discord Labs?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q3=res.content

            embed=discord.Embed(title="Application: Support Staff",description=F"**Almost Final Question: ** List your previous experiences in this position.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q4=res.content

            embed=discord.Embed(title="Application: Support Staff",description=F"**Final Question: ** What makes you different from other candidates?.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q5=res.content 

            embed=discord.Embed(title="Application: Support Staff",description=F"**Name:** {first} {last}.\n**Official Website:** {q1}\n**Lab Services:** {q2}\n**Vanities:** {q3}\n**Previous Experience:** {q4}\n**What Makes You Different:** {q5}",color=self.bot.embed)
            await msg.edit(embed=embed)

            embed=discord.Embed(title="Thanks for applying!",description="We'll let you know if your accepted on April 15.",color=self.bot.embed)
            await channel.send(embed=embed)

        if reaction.emoji==moderator:
            def check(m):
                return (m.channel == channel and m.author==ctx.author)

            embed=discord.Embed(title="Application: Moderator",description=F"Allright, lets get started, what is your **First Name?**",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            first=res.content


            embed=discord.Embed(title="Application: Moderator",description=F"Nice to meet you, {first}. What is the **First** letter of your **Last Name?**",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            last=res.content

            embed=discord.Embed(title="Application: Moderator",description=F"Awesome, below we have listed several questions, reply with what you think the answer is. **First Question: ** What is the link to the official Discord Labs website?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q1=res.content

            embed=discord.Embed(title="Application: Moderator",description=F"**Second Question: ** What's the best way to cool down a dispute?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q2=res.content

            embed=discord.Embed(title="Application: Moderator",description=F"**Third Question: ** A bot starts spamming the server, what do you do?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q3=res.content

            embed=discord.Embed(title="Application: Moderator",description=F"**Almost Final Question: ** List your previous experiences in this position.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q4=res.content

            embed=discord.Embed(title="Application: Moderator",description=F"**Final Question: ** What makes you different from other candidates?.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q5=res.content 

            embed=discord.Embed(title="Application: Moderator",description=F"**Name:** {first} {last}.\n**Official Website:** {q1}\n**Best way to stop dispute:** {q2}\n**Bot spamming server:** {q3}\n**Previous Experience:** {q4}\n**What Makes You Different:** {q5}",color=self.bot.embed)
            await msg.edit(embed=embed)

            embed=discord.Embed(title="Thanks for applying!",description="We'll let you know if your accepted on April 15.",color=self.bot.embed)
            await channel.send(embed=embed)

        if reaction.emoji==approver:
            def check(m):
                return (m.channel == channel and m.author==ctx.author)

            embed=discord.Embed(title="Application: Approver",description=F"Allright, lets get started, what is your **First Name?**",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            first=res.content


            embed=discord.Embed(title="Application: Approver",description=F"Nice to meet you, {first}. What is the **First** letter of your **Last Name?**",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            last=res.content

            embed=discord.Embed(title="Application: Approver",description=F"Awesome, below we have listed several questions, reply with what you think the answer is. **First Question: ** What is the link to the official Discord Labs website?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q1=res.content

            embed=discord.Embed(title="Application: Approver",description="**Second Question: ** Read [docs.discordlabs.org](https://docs.discordlabs.org/docs).\nWhat are the rules regarding NSFW bots on the list? Can bots mention NSFW in there description?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q2=res.content

            embed=discord.Embed(title="Application: Approver",description=F"**Third Question: ** A bot is offline when you are reviewing it, what do you do?",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q3=res.content

            embed=discord.Embed(title="Application: Approver",description=F"**Almost Final Question: ** List your previous experiences in this position.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q4=res.content

            embed=discord.Embed(title="Application: Approver",description=F"**Final Question: ** What makes you different from other candidates?.",color=self.bot.embed)
            await msg.edit(embed=embed)
            res = await self.bot.wait_for('message', check=check)
            await res.delete()
            q5=res.content 

            embed=discord.Embed(title="Application: Approver",description=F"**Name:** {first} {last}.\n**Official Website:** {q1}\n**NSFW Bots:** {q2}\n**Bot Offline:** {q3}\n**Previous Experience:** {q4}\n**What Makes You Different:** {q5}",color=self.bot.embed)
            await msg.edit(embed=embed)

            embed=discord.Embed(title="Thanks for applying!",description="We'll review your answers and let you know if your ready to move to the next stage soon.",color=self.bot.embed)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        #print(payload)
        #print(payload.channel_id)
        #print(payload.emoji)
        channel=self.bot.get_channel(payload.channel_id)

        try:
            msg = await channel.fetch_message(payload.message_id)
        except:
            return
        zuser = self.bot.get_user(payload.user_id)
        if zuser.bot:
            return
        guild=self.bot.get_guild(payload.guild_id)
        if(payload.channel_id) != 698422778575192094:
            return

        if str(payload.emoji) != "\U0001f39f":
            return
        
        await msg.remove_reaction(payload.emoji,zuser)
        approver = guild.get_role(610461598821253121)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True,send_messages=True),
            zuser: discord.PermissionOverwrite(read_messages=True,send_messages=True),
            approver: discord.PermissionOverwrite(read_messages=True,send_messages=True)
        }
        
        name="certify-"+str(zuser.name)
        name.replace(" ", "-")
        channel = await guild.create_text_channel(name,overwrites=overwrites,category=self.bot.get_channel(694737424743530538),topic=F"Status: New Application | Created By: {zuser.name}#{zuser.discriminator}")

        embed=discord.Embed(title="Ticket Created!",description=F"{zuser.mention}, your application has been created in {channel.mention}",color=self.bot.embed)
        mchannel=self.bot.get_channel(payload.channel_id)
        await mchannel.send(embed=embed,delete_after=10)
        await channel.send(content=zuser.mention,delete_after=1)
        embed=discord.Embed(title="Welcome to your application! Please answer the following questions to get started.",description=F"What is the ID of your Discord Bot?",color=self.bot.embed)
        msg=await channel.send(embed=embed)

        def check(m):
            return (m.channel == channel and m.author==zuser)
        s = False
        while not s:
            res = await self.bot.wait_for('message', check=check)
            bid = res.content
            await res.delete()
            query={"id":str(bid)}
            mydoc = self.bot.b.find(query)
            for x in mydoc:
                s=True
            if (not s):
                embed=discord.Embed(description=F"No bot with ID {str(bid)} was found on the [bot list](https://bots.discordlabs.org)",color=self.bot.embed)
                await channel.send(embed=embed,delete_after=5)
        print
        embed=discord.Embed(title=F"Certification Application",description=F"**How many servers is your bot in? (At the time of writing)**",color=self.bot.embed)
        await msg.edit(embed=embed)
        res = await self.bot.wait_for('message', check=check)
        guilds = res.content
        await res.delete()

        embed=discord.Embed(title=F"Certification Application",description=F"**How is your bot hosted?**",color=self.bot.embed)
        await msg.edit(embed=embed)
        res = await self.bot.wait_for('message', check=check)
        host = res.content
        await res.delete()

        embed=discord.Embed(title=F"Certification Application",description=F"**Describe the unique functionalities of your bot in 3-4 lines.**",color=self.bot.embed)
        await msg.edit(embed=embed)
        res = await self.bot.wait_for('message', check=check)
        unique = res.content
        await res.delete()

        embed=discord.Embed(title=F"Please Confirm",description=F"**Bot:** [{x['name']}](https://bots.discordlabs.org/bot/{x['url']})\n**Server Count:** {guilds}\n**Host:** {host}\n**Unique Functionality:** {unique}\n\n**Please react with :white_check_mark: to continue or with :x: to close this ticket.**",color=self.bot.embed)
        await msg.edit(embed=embed)
        await msg.add_reaction("\U00002705")
        await msg.add_reaction("\U0000274c")
        def reactioncheck(reaction,user):
            if (not user.bot):
                if reaction.message.id==msg.id:
                    if reaction.emoji in ["\U00002705","\U0000274c"]:
                        return True
            return False
        reaction, user = await self.bot.wait_for("reaction_add", check=reactioncheck)
        await msg.clear_reactions()
        if reaction.emoji=="\U00002705":
            await channel.send("@everyone",delete_after=1)
            embed=discord.Embed(title="Success!",description="Your application has been sent for review, please stand by.",color=self.bot.embed)
            await channel.send(embed=embed)

        else:
            await channel.send("Closing in 5 seconds")
            await asyncio.sleep(5)
            await channel.delete()
             



    
        
def setup(bot): 
    bot.add_cog(Update(bot))
