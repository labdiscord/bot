import discord 
from discord.ext import commands 
from pymongo import MongoClient  as mcl
import asyncio

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="certify")
    async def certify(self,ctx,bot:discord.Member=None):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return
        if (not bot):
            return await ctx.send("Correct usage is ?certify @bot")
        if (not bot.bot):
            return await ctx.send("Correct usage is ?certify @bot")
        mydoc=self.bot.b.find({"id":str(bot.id)})
        found=False
        for x in mydoc:
            found=True
        if (not found):
            return await ctx.send(F"No bot found with ID `{bot.id}`")
        update={"certification":True}
        self.bot.b.update_one({"id":str(bot.id)},{"$set":update})

        botdevr = ctx.guild.get_role(672176803204300817)
        botr = ctx.guild.get_role(672177486028734504)

        await bot.add_roles(botr)
        owner = ctx.guild.get_member(int(x["owner"][0]))
        await owner.add_roles(botdevr)

        for j in x["editor"]:
            try:
                e = ctx.guild.get_member(int(j))
            except:
                await e.add_roles(botdevr)
        return await ctx.send(F"Bot has been certified!")

    @commands.command(name="viewvanity",aliases=["vanity"])
    async def viewvanity(self,ctx,bot:discord.Member=None):
        if (not bot):
            return await ctx.send("Correct usage is ?viewvanity @bot")
        if (not bot.bot):
            return await ctx.send("Correct usage is ?viewvanity @bot")
        mydoc=self.bot.b.find({"id":str(bot.id)})
        found=False
        for x in mydoc:
            found=True
        if (not found):
            return await ctx.send(F"No bot found with ID `{bot.id}`")
        return await ctx.send(F"`{bot.id}`'s vanity is currently `{x['url']}` (https://dbots.cc/{x['url']})")


    @commands.command(name="setvanity")
    async def setvanity(self,ctx,bot:discord.Member=None,new=None):
        role=ctx.guild.get_role(608714147378626570)
        if role not in ctx.author.roles:
            return
        if (not bot or not new):
            return await ctx.send("Correct usage is ?setvanity @bot newvanity")
        if (not bot.bot):
            return await ctx.send("Correct usage is ?setvanity @bot newvanity")
        mydoc=self.bot.b.find({"id":str(bot.id)})
        found=False
        for x in mydoc:
            found=True
        if (not found):
            return await ctx.send(F"No bot found with ID `{bot.id}`")
        
        update={"url":new}
        self.bot.b.update_one({"id":str(bot.id)},{"$set":update})
        return await ctx.send(F"`{bot.id}`'s new vanity is `{new}` (https://dbots.cc/{new})")
        
        
def setup(bot): 
    bot.add_cog(Update(bot))
