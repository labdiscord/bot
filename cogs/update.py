import discord 
from discord.ext import commands, tasks
from pymongo import MongoClient  as mcl
import asyncio

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_users.start()
        self.botStatusUpdate.start()

    @commands.Cog.listener()
    async def on_member_join(self,member):
        if (not member.bot):
            return
        query={"id":str(member.id)}
        mydoc = self.bot.b.find(query)
        found=False
        for x in mydoc:
            found=True
        if not found:
            role=member.guild.get_role(608714199425613874)
            c=self.bot.get_channel(672175721413738517)
            return await c.send(F"{role.mention} <a:siren:689141551326035982> {member.mention} is not on the bot list but has been added to the server.")
        role=member.guild.get_role(672177210903363617)
        await member.add_roles(role)

    @tasks.loop(minutes=5)
    async def botStatusUpdate(self):
        channel = self.bot.get_channel(689114316515180579) # channel ID goes here
        guild=self.bot.get_guild(608711879858192479)
        
        count=0
        data=self.bot.b.find({})
        mydoc=[]
        for x in data:
            mydoc.append(x)
            embed=discord.Embed(title="Status Update Started",description=F"Updating data's of all bots.\n\nTotal Bots: {len(mydoc)}",color=self.bot.embed)
        m=await channel.send(embed=embed)
        online=0
        away=0
        dnd=0
        offline=0
        kicked=0
        olist=""
        for bot in mydoc:
            b = None
            try:
                b = guild.get_member(int(bot["id"]))
            except:
                pass
            if (b):
                s=str(b.status)
                if (s=="online" or s=="streaming"):
                    online+=1
                elif (s=="offline"):
                    offline+=1
                    olist+=(str(b.mention))+"\n"
                elif (s=="idle"):
                    away+=1
                elif (s=="dnd" or s=="do_not_disturb"):
                    dnd+=1
                avatar="https://cdn.discordapp.com/avatars/"+str(b.id)+"/"+b.avatar
                #if bot["status"]!="offline" and s=="offline":
                #    m=self.bot.get_channel(689164573831725086)
                #    await m.send(F"<@{bot['owner'][0]}>, your bot {b.mention} is currently offline.")
                #if bot["status"]=="offline" and s!="offline":
                #    m=self.bot.get_channel(689164573831725086)
                #    await m.send(F"<@{bot['owner'][0]}>, your bot {b.mention} is back online!")
                update={"status":s,"name":b.name,"avatar":avatar}
                    
            else:
                kicked+=1
                s="kicked"
                update={"status":"kicked"}

            query={"id":bot["id"]}
            update={"$set":update}
            self.bot.b.update_one(query,update)
            owner=bot["owner"][0]
            o = None
            try:
                o = guild.get_member(int(owner))
            except:
                pass
            cd=self.bot.get_channel(689114316515180579)
            if o:
                pass
                #await cd.send(F"<@{bot['id']}> owned by <@{owner}> PASSED")
            else:
                await cd.send(F"<@{bot['id']}> owned by <@{owner}> FAILED")

            # At this point, system gives all editors & owners bot dev role.
            botdev = guild.get_role(672176587449565233)
            try:
                await o.add_roles(botdev)
            except:
                pass
            for j in bot["editor"]:
                try:
                    u = guild.get_member(int(j))
                    await u.add_roles(botdev)
                except:
                    pass


                
                

                
                
            count+=1
            if count==5:
                embed=discord.Embed(title="Status Update In Progress",description=F"Updating data's of all bots.\n\n Progress: {str(count)}/{str(len(mydoc))}",color=self.bot.embed)
                await m.edit(embed=embed)
                count=0
                
        embed=discord.Embed(title="Data Update Ended",description=F"Total Bots: {len(mydoc)}\n\nOnline Bots: {online}\nAway Bots: {away}\nDND Bots: {dnd}\nKicked Bots: {kicked}\n\n**Offline Bots:** {offline}\nOffline Bots: {olist}",color=self.bot.embed)
        await m.edit(embed=embed)
        await asyncio.sleep(300) # task runs every 5 mins
    
    @tasks.loop(minutes=5)
    async def check_users(self):
        # get the server 
        server = self.bot.get_guild(608711879858192479)
        # get all the roles you want to be checked
        bot_dev = server.get_role(672176587449565233)
        certified_bot_dev = server.get_role(672176803204300817) 
        bots = server.get_role(672177210903363617)
        certified_bots = server.get_role(672177486028734504)

        role=server.get_role(608714199425613874)
        c=self.bot.get_channel(672175721413738517)

        data=self.bot.b.find({})
        mydoc=[]
        for x in data:
            mydoc.append(x)
        
        # go through every member that is in the server 
        for user in server.members:
            # i'm thinking

            if bot_dev in user.roles:
                found = False
                for x in mydoc:
                    if x["owner"][0] == str(user.id):
                        found=True
                    for j in x["editor"]:
                        if j==str(user.id):
                            found=True
                if not found:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is does not have a bot on the bot list but has the bot dev role.")

            if certified_bot_dev in user.roles:
                found = False
                val = False
                for x in mydoc:
                    if x["owner"][0] == str(user.id):
                        found=True
                    for j in x["editor"]:
                        if j==str(user.id):
                            found=True
                            var = x
                if not found:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is does not have a bot on the bot list but has the certified bot dev role.")
                if val and not val["certification"]:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is does not have a Certified bot on the bot list but has the certified bot dev role.")
                


            if bots in user.roles:
                data=self.bot.b.find({"id":str(user.id)})
                found=False
                for x in data:
                    found=True
                if not found:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is not on the bot list but has the bots role.")
            
            if certified_bots in user.roles:
                data=self.bot.b.find({"id":str(user.id)})
                found=False
                for x in data:
                    found=True
                if not found:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is not on the bot list but has the certified bots role.")
                elif not x["certification"]:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is not marked as certified on the bot list but has the bots role.")
        # tada | wot.


def setup(bot): 
    bot.add_cog(Update(bot))


