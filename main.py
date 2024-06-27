import os
import discord
from discord.ext import commands
from discord import app_commands
from colorama import Back, Fore, Style
import time
import platform
from discord import ui
from discord.ui import Button, View
from discord.utils import get
import requests, json, random, datetime
import asyncio
import datetime
from discord.ext import tasks

def is_owner(interaction: discord.Interaction):
  if interaction.user.id == 776121338402045962:
    return True
  return False

def kaizen(interaction: discord.Interaction):
  if interaction.guild.id == 1130934962061852819:
    return True
  return False

def spp(interaction: discord.Interaction):
  if interaction.guild.id == 1147529313667784734:
    return True
  return False
# This bot is created by anismondal


# ---------------------------------------------------------------------------------------------------------------------------

class verifyModal(ui.Modal, title="Kaizen Verification Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)

    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)

    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)


    async def on_submit(self, interaction: discord.Interaction):

        await interaction.user.edit(nick=f'{self.firstname} {self.lastname} - {self.yourid}')

        role = discord.utils.get(
            interaction.guild.roles, id=1097554918304395404)

        await interaction.user.add_roles(role)

        await interaction.response.send_message(

            f"{interaction.user.mention} **You Have Successfully Registered Into Kaizen**", ephemeral=True)

        channel = discord.utils.get(
            interaction.guild.channels, name="verified")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention}", colour=discord.Colour.random())
        embed.add_field(name=f"\n\n**Name**: {self.firstname} {self.lastname}", value=f"\n**ID:** {self.yourid}", inline=False)
        embed.set_footer(text="Successfully Verified")
        await channel.send(embed=embed)


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(
            '.'), intents=discord.Intents().all())
    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='god power', url='https://discord.gg/pYz2SYNmes'))
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='Grand RP'))
        prfx = (Back.BLACK + Fore.GREEN +
                time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET +
                Fore.WHITE + Style.BRIGHT)
        print(prfx + " Logged in as " + Fore.YELLOW + self.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(self.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        print(prfx + " Python version " + Fore.YELLOW +
              str(platform.python_version()))
        synced = await self.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) +
              " Commands")
        channel = client.get_channel(1132023129561108501)
        await channel.send("The Bot is online")
        # afk = client.get_channel(1131257471059644566)
        # await afk.send(afk)
        # task_loop.start()
        # await schedule_daily_message()
        # await schedule_daily_message2()


client = Client()


@client.tree.command(name="verify", description="verify")
@app_commands.check(is_owner)
async def verify(interaction: discord.Interaction):

    role1 = Button(label="Click To Verify ", style=discord.ButtonStyle.green, emoji="<a:02:1078270464000012319>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(verifyModal())

    role1.callback = role1_callback
    view = View(timeout=None)
    view.add_item(role1)
    embed = discord.Embed(
        title="**WELCOME TO KAIZEN FAMILY**\n\n\n",
        description="**Our Family Serves as the best Indian family in Grand RP** \n\n**__In order to verify yourself just click on the below button and fill all the details__**\n**After Submitting the form you will be verified.**",
        color=5763719)

    embed.set_image(
        url="https://media.discordapp.net/attachments/1133102948516364379/1133104735294074920/standard_10.gif")

    await interaction.response.send_message("Verify button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)


@verify.error
async def verify_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)


# --------------------------------------------------------------------------------------------------------------------------


class nameModal(ui.Modal, title="Kaizen Name Change Form"):

    previousname = ui.TextInput(label="Your Previous Name With ID", placeholder="Anis Kaizen - 263907", required=True, style=discord.TextStyle.short)

    newfirstname = ui.TextInput(label="Your New First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)

    newlastname = ui.TextInput(label="Your New Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)

    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.user.edit(nick=f'{self.newfirstname} {self.newlastname} - {self.yourid}')

        await interaction.response.send_message(f"{interaction.user.mention} **Your name was successfully changed**", ephemeral=True)

        channel = discord.utils.get(interaction.guild.channels, name="name-change-logs")

        
        embed = discord.Embed(description=f"**Player:** {interaction.user.mention}", colour=discord.Colour.random())
        embed.add_field(name=f"\n\n**Previous Name:** {self.previousname} \n**New Name:** {self.newfirstname} {self.newlastname}", value=f"\n**ID:** {self.yourid}", inline=False)
        embed.set_footer(text="Successfully Changed Name")
        await channel.send(embed=embed)

@client.tree.command(name="rename", description="rename")
@app_commands.check(is_owner)
async def rename(interaction: discord.Interaction):
    role1 = Button(label="Click To Change Name", style=discord.ButtonStyle.green, emoji="<a:tick:1078350710430761071>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(nameModal())
    role1.callback = role1_callback
    view = View(timeout=None)
    view.add_item(role1)
    embed = discord.Embed(
        title="**Kaizen Name Change Form**",
        description="**\n\nIn order to change your name**\nClick the below button\nFill in the details\nAfter Submitting it your name will be changed.",
        color=5763719)
    embed.set_image(
        url="https://media.discordapp.net/attachments/1133102948516364379/1133105026479431711/standard_11.gif")

    await interaction.response.send_message("Rename button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)

@rename.error
async def rename_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)



# ------------------------------------------------------------------------------------------------------------------------


class loaModal(ui.Modal, title="LOA Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)
    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)
    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)
    days = ui.TextInput(label="No Of Days", placeholder="1-30", required=True, style=discord.TextStyle.short)
    reason = ui.TextInput(label="Reason", placeholder="OOC Work", required=True, style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.user.edit(nick=f'LOA | {self.firstname} {self.lastname} | {self.yourid}')
        role = discord.utils.get(interaction.guild.roles, id=1099596560196706314)
        await interaction.user.add_roles(role)
        await interaction.response.send_message(f"{interaction.user.mention} **Your LOA application has been submitted, have a safe journey ahead**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="loa-logs")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention} \n\n**ID:** {self.yourid}", colour=discord.Colour.random())
        embed.add_field(name=f"\n**Days:** {self.days}", value=f"\n**Reason:** {self.reason}\n\n**Roles Added:** <@&1099596560196706314>", inline=False)
        await channel.send(embed=embed)

class removeloaModal(ui.Modal, title="Remove LOA Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)
    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)
    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.user.edit(nick=f'{self.firstname} {self.lastname} - {self.yourid}')
        roles = interaction.channel.guild.get_role(1099596560196706314)
        await interaction.user.remove_roles(roles)
        await interaction.response.send_message(f"{interaction.user.mention} **Your LOA application has been submitted, have a safe journey ahead**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="loa-logs")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention} \n\n**ID:** {self.yourid}", colour=discord.Colour.random())
        embed.add_field(name=f"\nIs Back From His LOA", value="\n\n**Roles Removed:** <@&1099596560196706314>", inline=False)
        await channel.send(embed=embed)
        







@client.tree.command(name="loa", description="LOA")
@app_commands.check(is_owner)
async def loa(interaction: discord.Interaction):

    role1 = Button(label="Click for LOA", style=discord.ButtonStyle.green, emoji="<a:76:1005564928297541742>")
    role2 = Button(label="Click To Remove LOA", style=discord.ButtonStyle.red, emoji="<a:81:1005562828574437376>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(loaModal())

    async def role2_callback(interaction2):
        await interaction2.response.send_modal(removeloaModal())

    role1.callback = role1_callback
    role2.callback = role2_callback
    view = View(timeout=None)
    view.add_item(role1)
    view.add_item(role2)
    embed = discord.Embed(
        title="Kaizen Family Leave Of Application",
        description="**__In order to take LOA yourself just click on the below button and fill all the details__**\n**After Submitting the form you will be given LOA.**",
        color=5763719)

    embed.set_image(
        url="https://media.discordapp.net/attachments/1133102948516364379/1133106906563616768/standard_14.gif")


    await interaction.response.send_message("LOA button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)


@loa.error
async def loa_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)

# ---------------------------------------------------------------------------------------------------------------------------


class examModal(ui.Modal, title="Exam Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)
    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)
    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)
    rank = ui.TextInput(label="Rank", placeholder="Rank 3", required=True, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} **Your LOA application has been submitted, have a safe journey ahead**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="exam-request-logs")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention} \n\n**ID:** {self.yourid} \n**Request Exam For Rank:** {self.rank}", colour=discord.Colour.random())
        await channel.send(embed=embed)


@client.tree.command(name="exam", description="exam")
@app_commands.check(is_owner)
async def exam(interaction: discord.Interaction):

    role1 = Button(label="Click To Request Exam", style=discord.ButtonStyle.blurple, emoji="<a:02:1078270464000012319>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(examModal())

    role1.callback = role1_callback
    view = View(timeout=None)
    view.add_item(role1)
    embed = discord.Embed(
        title="Exam Request",
        description="**\n\nIn order to request exam**\nClick the below button\nFill in the details\n__After Submitting you request will be sent and wait for any HRT to verify it.__",
        color=5763719)

    embed.set_image(
        url="https://media.discordapp.net/attachments/1133102948516364379/1133107661076963398/standard_15.gif")

    await interaction.response.send_message("Exam button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)


@exam.error
async def exam_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)


# ----------------------------------------------------------------------------------------------------------------------------


class afkModal(ui.Modal, title="AFK Form"):

    afk = ui.TextInput(label="City Time", placeholder="13:13", required=True, style=discord.TextStyle.short)
    

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} **You are now afk no one will disturbe you.**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="afk-logs")
        embed = discord.Embed(description=f"**Player:** {interaction.user.mention} \n\n**From:** {self.afk}", colour=0xe74c3c)
        await channel.send(embed=embed)

        role = discord.utils.get(interaction.guild.roles, id=1138522067734642829)

        await interaction.user.add_roles(role)


class removeafkModal(ui.Modal, title="AFK Form"):

    removeafk = ui.TextInput(label="City Time", placeholder="13:13", required=True, style=discord.TextStyle.short)
    

    async def on_submit(self, interaction: discord.Interaction):
        roles = interaction.channel.guild.get_role(1138522067734642829)
        await interaction.user.remove_roles(roles)
        await interaction.response.send_message(f"{interaction.user.mention} **You are now back online.**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="afk-logs")
        embed = discord.Embed(description=f"**Player:** {interaction.user.mention} \n\n**Back At:** {self.removeafk}", colour=0x2ecc71)
        await channel.send(embed=embed)






@client.tree.command(name="afk", description="afk")
@app_commands.check(is_owner)
async def afk(interaction: discord.Interaction):
    role1 = Button(label="Click For AFK", style=discord.ButtonStyle.green, emoji="<a:76:1005564928297541742>")
    role2 = Button(label="Click To Remove AFK", style=discord.ButtonStyle.red, emoji="<a:81:1005562828574437376>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(afkModal())

    async def role2_callback(interaction2):
        await interaction2.response.send_modal(removeafkModal())



    role1.callback = role1_callback
    role2.callback = role2_callback
    view = View(timeout=None)
    view.add_item(role1)
    view.add_item(role2)
    embed = discord.Embed(
        title="AFK",
        description="**Click the below button to go for AFK**",
        color=5763719)


    await interaction.response.send_message("AFK button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)
    




@afk.error
async def afk_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)


# -----------------------------------------------------------------------------------------------------------------------------


class roleModal(ui.Modal, title="Role Request Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)
    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)
    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)
    role = ui.TextInput(label="Role", placeholder="rank 3", required=True, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} **Your Role Request application has been submitted**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="role-request-logs")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention}", colour=discord.Colour.random())
        embed.add_field(name=f"\n\n**Name:** {self.firstname} {self.lastname} \n**ID:** {self.yourid}", value=f"\n**Role Requested:** {self.role}", inline=False)
        await channel.send(embed=embed)



@client.tree.command(name="rolerequest", description="rolerequest")
@app_commands.check(is_owner)
async def role(interaction: discord.Interaction):

    role1 = Button(label="Click To Request Role", style=discord.ButtonStyle.blurple, emoji="<a:02:1078270464000012319>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(roleModal())

    role1.callback = role1_callback
    view = View(timeout=None)
    view.add_item(role1)
    embed = discord.Embed(
        title="Role Request",
        description="**\n\nIn order to Request Rank**\nClick the below button\nFill in the details.\n__After Submitting Wait till hc to verify and you will be provided with the rank__",
        color=5763719)



    await interaction.response.send_message("Request button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)


@role.error
async def role_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)



# -------------------------------------------------------------------------------------------------------------------------------------



class sppverifyModal(ui.Modal, title="SPP Verification Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)

    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)

    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)


    async def on_submit(self, interaction: discord.Interaction):

        await interaction.user.edit(nick=f'{self.firstname} {self.lastname} - {self.yourid}')

        role = discord.utils.get(
            interaction.guild.roles, id=1147630220912902405)

        await interaction.user.add_roles(role)

        await interaction.response.send_message(

            f"{interaction.user.mention} **You Have Successfully Registered Into Grand RP Solar Panel Plantation**", ephemeral=True)

        channel = discord.utils.get(
            interaction.guild.channels, name="verified")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention}", colour=discord.Colour.random())
        embed.add_field(name=f"\n\n**Name**: {self.firstname} {self.lastname}", value=f"\n**ID:** {self.yourid}", inline=False)
        embed.set_footer(text="Successfully Verified")
        await channel.send(embed=embed)



@client.tree.command(name="sppverify", description="verify")
@app_commands.check(is_owner)
async def verify(interaction: discord.Interaction):

    role1 = Button(label="Click To Verify ", style=discord.ButtonStyle.green, emoji="<a:02:1078270464000012319>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(sppverifyModal())

    role1.callback = role1_callback
    view = View(timeout=None)
    view.add_item(role1)
    embed = discord.Embed(
        title="**WELCOME TO SOLAR PANEL PLANTATION**\n\n\n",
        description="**Plant Solar Panels and Earn A Lot Of Money** \n\n**__In order to verify yourself just click on the below button and fill all the details__**\n**After Submitting the form you will be verified.**",
        color=5763719)

    embed.set_image(
        url="https://media.discordapp.net/attachments/1133102948516364379/1147632537607340163/standard_16.gif")

    await interaction.response.send_message("Verify button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)





class sppModal(ui.Modal, title="SPP Request Form"):

    firstname = ui.TextInput(label="Your First Name", placeholder="Anis", required=True, style=discord.TextStyle.short)
    lastname = ui.TextInput(label="Your Last Name", placeholder="Kaizen", required=True, style=discord.TextStyle.short)
    yourid = ui.TextInput(label="ID", placeholder="263907", required=True, style=discord.TextStyle.short)
    rank = ui.TextInput(label="Reason", placeholder="To earn money", required=True, style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"{interaction.user.mention} **Your SPP Request application has been submitted, please wait for the HC to review it**", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="spp-request")

        embed = discord.Embed(description=f"**Player:** {interaction.user.mention} \n\n**ID:** {self.yourid} \n**Request Exam For Rank:** {self.rank}", colour=discord.Colour.random())
        await channel.send(embed=embed)





@client.tree.command(name="plantationrequest", description="plantation request")
@app_commands.check(is_owner)
async def spp(interaction: discord.Interaction):

    role1 = Button(label="Click To Join Solar Plantation", style=discord.ButtonStyle.blurple, emoji="<a:02:1078270464000012319>")
    async def role1_callback(interaction1):
        await interaction1.response.send_modal(sppModal())

    role1.callback = role1_callback
    view = View(timeout=None)
    view.add_item(role1)
    embed = discord.Embed(
        title="Solar Plantation Request",
        description="**\n\nIn order to join Solar Plantation Group**\nClick the below button\nFill in the details\n__After Submitting you request will be sent and wait for any HC to verify it.__",
        color=5763719)

    embed.set_image(
        url="https://media.discordapp.net/attachments/1133102948516364379/1147637215900487850/standard_17.gif")

    await interaction.response.send_message("Exam button <a:02:1078270464000012319> sent successfully", ephemeral=True)
    await interaction.channel.send(embed=embed, view=view)
    await interaction.response.send_message(embed=embed, view=view)


@spp.error
async def spp_error(interaction: discord.Interaction, error):
  await interaction.response.send_message("You are not my owner", ephemeral=True)











# async def schedule_daily_message():
#     now = datetime.datetime.now()
#     then = now+datetime.timedelta(days=1)
#     then = now.replace(hour=00, minute=36)
#     wait_time = (then-now).total_seconds()
#     await asyncio.sleep(wait_time)

#     channel = client.get_channel(1132016189804134551)

#     await channel.send("Hello there to all")



# async def schedule_daily_message2():
#     now = datetime.datetime.now()
#     then = now+datetime.timedelta(days=1)
#     then = now.replace(hour=00, minute=37)
#     wait_time = (then-now).total_seconds()
#     await asyncio.sleep(wait_time)

#     channel = client.get_channel(1132016189804134551)

#     await channel.send("Good Night")

# @tasks.loop(hours=6)
# async def task_loop():
#     channel = client.get_channel(1132016189804134551)

#     # await channel.send("Hello There to all my fellows")

#     embed = discord.Embed(description= "**__Don't Forget To Post Your Office Task Logs Before Tsunami!!!__**", colour=discord.Colour.random())
#     embed.set_author(name="Horizon INC - 158045", icon_url="https://media.discordapp.net/attachments/1001075059802251284/1113510770471350312/Gold_and_Black_Buildings_Flat_Illustrative_Real_Estate_Service_Animated_Logo_3.jpg")
#     embed.set_image(url="https://media.discordapp.net/attachments/1001075059802251284/1113412342743580764/standard_18.gif")
#     embed.set_footer(icon_url="https://media.discordapp.net/attachments/1001075059802251284/1113510770471350312/Gold_and_Black_Buildings_Flat_Illustrative_Real_Estate_Service_Animated_Logo_3.jpg", text="Horizon INC (Let Your Dreams Come True)")
#     await channel.send("@everyone", embed=embed)











# @client.tree.command(name="hello", description="Testing hello")
# @app_commands.check(is_owner)
# async def hello(interaction=discord.Interaction):
#     await interaction.response.send_message(f"Hello there {interaction.user.mention} ", ephemeral=True)

# @hello.error
# async def hello_error(interaction: discord.Interaction, error):
#   await interaction.response.send_message("Not allowed!", ephemeral=True)


client.run("MTEzMDkzMzAzODUyMDQ3OTg2NA.GSZXdI.6DLjpv0qGFD-MxMehxCiIvWYJ1bu1Q6J2S6FqI")
