import discord 
from discord.ext import commands 

class Reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # get the message id from payload
        message = payload.message_id 
        # this will see if the payload message id is the same as another message id
        if message == 713988101193859092:
            # get the guild id from payload
            guild_id = payload.guild_id
            guild = self.bot.get_guild(guild_id)
            print(payload.emoji.name)
            # see if the payload emoji name is the same as another one 
            if payload.emoji.name == "announcement":
                # get the role
                role = discord.utils.get(guild.roles, name="Announcements Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles by the <a:announcement:632970424837210131> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role by clicking the <a:announcement:632970424837210131> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role by clicking the <a:announcement:632970424837210131> reaction!", delete_after=4)
            elif payload.emoji.name == "updates":
                # get the role
                role = discord.utils.get(guild.roles, name="Updates Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles by the <a:updates:713984949732245624> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role by clicking the <a:updates:713984949732245624> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role by clicking the <a:updates:713984949732245624> reaction!", delete_after=4)
            elif payload.emoji.name == "siren":
                # get the role
                role = discord.utils.get(guild.roles, name="Incidents Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles by the <a:siren:689141551326035982> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role by clicking the <a:siren:689141551326035982> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role by clicking the <a:siren:689141551326035982> reaction!", delete_after=4)
            elif payload.emoji.name == "poll":
                # get the role
                role = discord.utils.get(guild.roles, name="Poll Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles by the <:poll:713986895884976154> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role by clicking the <:poll:713986895884976154> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role by clicking the <:poll:713986895884976154> reaction!", delete_after=4)            
            elif payload.emoji.name == "staff":
                # get the role
                role = discord.utils.get(guild.roles, name="Applications Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.add_roles(role, reason="Reaction roles by the <:staff:713984949639708712> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have gotten the **{role.name}** role by clicking the <:staff:713984949639708712> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have gotten the **{role.name}** role by clicking the <:staff:713984949639708712> reaction!", delete_after=4)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
       # get the message id from payload
       message = payload.message_id 
       # this will see if the payload message id is the same as another message id
       if message == 713988101193859092:
            # get the guild id from payload
            guild_id = payload.guild_id
            guild = self.bot.get_guild(guild_id)
            print(payload.emoji.name)
            # see if the payload emoji name is the same as another one 
            if payload.emoji.name == "announcement":
                # get the role
                role = discord.utils.get(guild.roles, name="Announcements Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.remove_roles(role, reason="Reaction roles by the <a:announcement:632970424837210131> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role by clicking the <a:announcement:632970424837210131> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role by clicking the <a:announcement:632970424837210131> reaction!", delete_after=4)
            elif payload.emoji.name == "updates":
                # get the role
                role = discord.utils.get(guild.roles, name="Updates Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.remove_roles(role, reason="Reaction roles by the <a:updates:713984949732245624> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role by clicking the <a:updates:713984949732245624> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role by clicking the <a:updates:713984949732245624> reaction!", delete_after=4)
            elif payload.emoji.name == "siren":
                # get the role
                role = discord.utils.get(guild.roles, name="Incidents Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.remove_roles(role, reason="Reaction roles by the <a:siren:689141551326035982> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role by clicking the <a:siren:689141551326035982> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role by clicking the <a:siren:689141551326035982> reaction!", delete_after=4)
            elif payload.emoji.name == "poll":
                # get the role
                role = discord.utils.get(guild.roles, name="Poll Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.remove_roles(role, reason="Reaction roles by the <:poll:713986895884976154> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role by clicking the <:poll:713986895884976154> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role by clicking the <:poll:713986895884976154> reaction!", delete_after=4)            
            elif payload.emoji.name == "staff":
                # get the role
                role = discord.utils.get(guild.roles, name="Applications Notify")

                # get the user
                user = guild.get_member(payload.user_id)

                # add the role to the user
                await user.remove_roles(role, reason="Reaction roles by the <:staff:713984949639708712> emoji.")

                # send a mesage to the user saying that they have successfully gottn the role
                try:
                    print("Trying to dm the user")
                    await user.send(f":tada: You have removed the **{role.name}** role by clicking the <:staff:713984949639708712> reaction!")
                except:
                    print("Couldn't dm the user, so I am going to try and send the message in the channel.")
                    # get the channel so that it can notify them there
                    channel = guild.get_channel(713983354428456961)

                    # send the congrats message there 
                    # delete after 4 seconds so that it doesn't flood the chat
                    await channel.send(f":tada: {user.mention}, you have removed the **{role.name}** role by clicking the <:staff:713984949639708712> reaction!", delete_after=4)
def setup(bot):
    bot.add_cog(Reaction(bot))