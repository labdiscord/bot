import discord 
from discord.ext import commands, tasks
from pymongo import MongoClient  as mcl
import asyncio
import requests
import sys

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_users.start()
        self.botStatusUpdate.start()
        print("hmk")

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
        print("hokay")
        debug = True
        try:
            print('----------')
            print("Status Updates")
            channel = self.bot.get_channel(689114316515180579) # channel ID goes here
            guild=self.bot.get_guild(608711879858192479)
            
            count=0
            data=self.bot.b.find()
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
            #The start of pain (WHO CODES LIKE THIS)
            for bot in mydoc:
                try:
                    b = None
                    try:
                        b = guild.get_member(int(bot["id"]))
                    except:
                        pass
                    if debug:
                        print(b)
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

                            
                        autocount = None
                        try:
                            autocount=bot["autocount"]
                        except:
                            pass
                        
                        if(autocount):
                            try:
                                a = b.activity
                                print(a)
                                #(a)
                                if (a):
                                    try:
                                        a = a.name
                                        nlist = [int(s) for s in a.split() if s.isdigit()]
                                        stat = (nlist[int(autocount["pos"])-1])
                                        if (autocount["type"]=='server'):
                                            update={"status":s,"name":b.name,"avatar":avatar,"guilds":int(stat),"shards":-1}
                                        elif (autocount["type"]=='shard'):
                                            update={"status":s,"name":b.name,"avatar":avatar,"guilds":-1,"shards":int(stat)}
                                        else:
                                            update={"status":s,"name":b.name,"avatar":avatar}
                                    except:
                                        update={"status":s,"name":b.name,"avatar":avatar}
                                        print("Failed to pull stats from presence.")
                                else:
                                    update={"status":s,"name":b.name,"avatar":avatar}
                            except:
                                update={"status":s,"name":b.name,"avatar":avatar}
                                if debug:
                                    print("Failed to pull stats from presence.")
                            
                        else:
                            update={"status":s,"name":b.name,"avatar":avatar}
                        statcord = None
                        try:
                            statcord=bot["statcord"]
                        except:
                            pass
                        if (statcord):
                            try:
                                #print(F"https://statcord.com/logan/stats/{bot['id']}")
                                response = requests.get(F"https://statcord.com/logan/stats/{bot['id']}")
                                if(response.status_code==200):
                                    data = response.json()
                                    data = data['data']
                                    data = data[len(data)-1]
                                    update={"status":s,"name":b.name,"avatar":avatar,"guilds":data['servers'],"shards":-1}
                                else:
                                    update={"status":s,"name":b.name,"avatar":avatar}
                            except:
                                update={"status":s,"name":b.name,"avatar":avatar}
                                if debug:
                                    print("Failed to pull stats from statcord.")
                        
                            
                    else:
                        kicked+=1
                        s="kicked"
                        update={"status":"kicked"}
                    
                    
                    query={"id":bot["id"]}
                    update={"$set":update}
                    try:
                        self.bot.b.update_one(query,update)
                    except:
                        if debug:
                            print("WARNING - UPDATE FAILED")
                            print(update)

                    
                    owner=bot["owner"][0]
                    o = guild.get_member(int(owner))
                    print("OWNER")
                    print(o)
                    try:
                        o = guild.get_member(int(owner))
                    except:
                        pass
                    print(o)
                    cd=self.bot.get_channel(689114316515180579)
                    if o:
                        # At this point, system gives all editors & owners bot dev role.
                        botdev = guild.get_role(672176587449565233)
                        try:
                            await o.add_roles(botdev)
                        except:
                            pass
                        if (bot["certification"]):
                            cbotdev = guild.get_role(672176803204300817)
                            try:
                                await o.add_roles(cbotdev)
                            except:
                                pass
                            for j in bot["editor"]:
                                try:
                                    u = guild.get_member(int(j))
                                    await u.add_roles(cbotdev)
                                except:
                                    pass
                        
                        nouptime = False
                        try:
                            nouptime=bot["nouptime"]
                        except:
                            nouptime = False
                        if (not nouptime):
                            print("currently")
                            print(bot["status"])
                            if bot["status"]!="offline" and s=="offline":
                                m=self.bot.get_channel(713552166006161508)
                                await m.send(F"<@{bot['owner'][0]}>, your bot {b.mention} is currently offline.")
                            if bot["status"]=="offline" and s!="offline":
                                m=self.bot.get_channel(713552166006161508)
                                await m.send(F"<@{bot['owner'][0]}>, your bot {b.mention} was offline but is now back online!")

                        # Bot Status Check Timeeee

                        checks = [0,0]
                        try:
                            checks = bot['checks']
                        except:
                            checks = [0,0]
                        if s=="offline" or s=="kicked":
                            if debug:
                                print("offline")
                            checks[1] = checks[1] + 1
                        else:
                            if debug:
                                print("online")
                            checks[0] = checks[0] + 1
                        query={"id":bot["id"]}
                        try:
                            update={"$set":{"checks":checks}}
                        except:
                            if debug:
                                print("WARNING - UPDATE FAILED")
                                print(update)
                        
                        self.bot.b.update_one(query,update)
                        if debug:
                            print("done")


                            
                        
                    else:
                        await cd.send(F"<@{bot['id']}> owned by <@{owner}> FAILED")
                            

                    count+=1
                    if count%5==0:
                        embed=discord.Embed(title="Status Update In Progress",description=F"Updating data's of all bots.\n\n Progress: {str(count)}/{str(len(mydoc))}",color=self.bot.embed)
                        await m.edit(embed=embed)
                except:
                    pass
                    
                    
            embed=discord.Embed(title="Data Update Ended",description=F"Total Bots: {len(mydoc)}\n\nOnline Bots: {online}\nAway Bots: {away}\nDND Bots: {dnd}\nKicked Bots: {kicked}\n\n**Offline Bots:** {offline}\nOffline Bots: {olist}",color=self.bot.embed)
            await m.edit(embed=embed)
            await asyncio.sleep(30) # task runs every .5 mins
            # The fact that someone wrote this is sad.
            
            #print("Stats Update Done")
            #print(F"Total Bots: {len(mydoc)}\n\nOnline Bots: {online}\nAway Bots: {away}\nDND Bots: {dnd}\nKicked Bots: {kicked}\n\n**Offline Bots:** {offline}\nOffline Bots: {olist}")
        except:
            print("Unexpected error:", sys.exc_info()[0])
    @tasks.loop(minutes=5)
    async def check_users(self):
        # get the server 
        server = self.bot.get_guild(608711879858192479)
        # get all the roles you want to be checked
        bot_dev = server.get_role(672176587449565233)
        certified_bot_dev = server.get_role(672176803204300817) 
        bots = server.get_role(672177210903363617)
        certified_bots = server.get_role(672177486028734504)
        unlisted = server.get_role(699405118965022750)

        role=server.get_role(608714199425613874)
        c=self.bot.get_channel(672175721413738517)

        data=self.bot.b.find({})
        mydoc=[]
        for x in data:
            mydoc.append(x)
        
        # go through every member that is in the server 
        for user in server.members:
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
                


            if bots in user.roles and unlisted not in user.roles:
                data=self.bot.b.find({"id":str(user.id)})
                found=False
                for x in data:
                    found=True
                if not found:
                    await c.send(F"{role.mention} <a:siren:689141551326035982> {user.mention} is not on the bot list but has the bots role.")
            
            if certified_bots in user.roles and unlisted not in user.roles:
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


