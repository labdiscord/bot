import discord
from discord.ext import commands 
from pymongo import MongoClient as mcl 
import os 
import sys
from dotenv import load_dotenv
load_dotenv()

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(),command_prefix=commands.when_mentioned_or('!'),help_command=None,activity=discord.Activity(name=' Over Discord Labs.', type=discord.ActivityType.watching),case_insensitive=True)

        self.check = ":white_check_mark:"
        self.x = ":x:"
        self.devs = [
            365958975201738764 # Anish
        ]
        
    

    async def on_command_error(self,ctx, error):
        if ctx.command.has_error_handler():
            return
        if isinstance(error,commands.MissingPermissions):
            ctx.reply(error.message)
        elif isinstance(error,commands.CheckAnyFailure):
            ctx.reply(error.message)
        elif isinstance(error,commands.MissingRole):
            ctx.reply(error.message)
        else:
            ctx.reply("An error occured")
    async def on_ready(self):
        print('Bot Started')
        #MongoDB Stuff
        self.client = mcl(os.getenv('MONGO_CONNECTION_URL'))
        self.db=self.client['main']
        self.b = self.db['bots']
        self.a = self.db['ads']
        self.q = self.db['queue']

        self.embed=0x800080

        channel=self.get_channel(698422778575192094)
        embed=discord.Embed(title="Certification Applications",description="React with :tickets: to apply for certification on [Discord Bot Labs](https://bots.discordlabs.org)\n\nMake sure your bot meets all the requirements listed on [docs.discordlabs.org/docs/certification/requirements](https://docs.discordlabs.org/docs/certification/requirements)",color=self.embed)
        #await channel.purge()
        #await channel.send(embed=embed)

        
        msg=await channel.history(limit=1, oldest_first=True).flatten()
        msg=msg[0]
        await msg.clear_reactions()
        await msg.add_reaction('\U0001f39f')  

        channel=self.get_channel(713983354428456961)
        embed=discord.Embed(title="Discord Labs - Get Roles",description="""React with <a:announcement:632970424837210131> to get to get pinged every time we make an announcement.\n
        React with <a:updates:713984949732245624> to get to get pinged every time we announce an update.\n
        React with <a:siren:689141551326035982> to get to get pinged for incidents/planned maintainence.\n
        React with <:poll:713986895884976154> to get to get pinged when we post a poll in <#689140582874087442>.\n
        React with <:staff:713984949639708712> to get to get pinged when we open staff applications.""",color=self.embed)
        #await channel.purge()
        #m = await channel.send(embed=embed)
        #await m.add_reaction("<a:announcement:632970424837210131>")
        #await m.add_reaction("<a:updates:713984949732245624>")
        #await m.add_reaction("<a:siren:689141551326035982>")
        #await m.add_reaction("<:poll:713986895884976154>")
        #await m.add_reaction("<:staff:713984949639708712>")
    



        for file in os.listdir('cogs'):
            if file.endswith('.py'):
                try:
                    print(f"Loading {file}")
                    self.load_extension(f'cogs.{file[:-3]}')
                except Exception as e:
                    print(e,file=sys.error)
bot = Bot()


@bot.command()
@commands.check(lambda x: x.id in bot.devs)
async def restart(ctx):
  await ctx.send(F"Restarting. This may take a little! Please be patient with me.")
  os.execv(sys.executable, [sys.executable]+sys.argv)
@bot.command()
@commands.check(lambda x: x.id in bot.devs)
async def reload(ctx, cog = None):
    if not cog:
        for cg in bot.cogs.keys():
            bot.reload_extension(cg)

    try:
        bot.reload_extension(cog)
        await ctx.send(F"{bot.check} Successfully reloaded **{cog}**!")
    except Exception as e:
        await ctx.send(f"{bot.x} Oh no! There was an error reloading **{cog}**!\n**({e})**")
bot.run(os.getenv("TOKEN"))
