import discord
from discord.ext import commands 
from pymongo import MongoClient as mcl 
import os 
import sys

TOKEN = "TOKEN"

cogs = [
    'cogs.certify',
    'cogs.update',
    'cogs.info',
    'cogs.ticket',
    'cogs.eval',
    'cogs.moderation',
    'cogs.anti-invite'
]

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="?", case_insensitve=True)

        self.check = ":white_check_mark:"
        self.x = ":x:"
        self.devs = [
            365958975201738764 # Anish
        ]
        

    async def on_ready(self):
        print(f"Bot is online!")

        activity = discord.Activity(name=' Over Discord Labs.', type=discord.ActivityType.watching)
        await bot.change_presence(activity=activity)
        print('Intilized successfully.')
        #MongoDB Stuff
        self.client = mcl('MONGODB CONNECTION URL')
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



        for cog in cogs:
            try:
                bot.load_extension(cog)
                print(f"Loaded {cog}")
            except Exception as e:
                print(e)

bot = Bot()
bot.remove_command('help')
@bot.command()
async def restart(ctx):
  if not ctx.author.id in bot.devs:
    return
  await ctx.send(F"Restarting. This may take a little! Please be patient with me.")
  await bot.change_presence(status = discord.Status.dnd, activity = discord.Game("RESTARTING BOT!"))
  os.execv(sys.executable, ['python3.6'] + sys.argv)
@bot.command()
async def reload(ctx, cog = None):
    if not ctx.author.id in bot.devs:
        return
    if not cog:
        return
    try:
        bot.reload_extension(cog)
        await ctx.send(F"{bot.check} Successfully reloaded **{cog}**!")
    except Exception as e:
        await ctx.send(f"{bot.x} Oh no! There was an error reloading **{cog}**!\n**({e})**")
bot.run(TOKEN)
