import discord
from discord.ext import commands
import asyncio
from flask import Flask
from threading import Thread
import os
import time

app = Flask('')



@app.route('/')
def home():
  return "I'm alive"



def run():
 app.run(host='0.0.0.0',port=8000)



def keep_alive():  
    t = Thread(target=run)
    t.start()
  
print(discord.__version__)
bot = commands.Bot(command_prefix="?")
cooldown = 20  
last_command = 0  

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def nmail(ctx, *, argument):
    if "@" in argument:
        user_id = 776713176532123668
        user = await bot.fetch_user(user_id)
        await user.send(f"v!cure {argument}")

        def check(message):
            return message.author.id == user_id

        try:
            response = await bot.wait_for("message", check=check, timeout=60)
            await ctx.send(f"{ctx.author.mention} Beginning GNAA-sponsored gay nigger conversion therapy for enemy heterosexual email.")
        except asyncio.TimeoutError:
            await ctx.send("Error occurred - unable to respond. contact GNAA agents for help.")

@bot.command()
async def stop(ctx):
    user_id = 776713176532123668  
    user = await bot.fetch_user(user_id)
    await user.send("v!stopcure")
    await ctx.send(f"Niggermail stopped.")

@bot.command()
async def private(ctx):
    author = ctx.author
    channel_name = f"{author.name}-channel"
    category_name = "niggermail distribution network"  


    category = discord.utils.get(ctx.guild.categories, name=category_name)
    if not category:
        await ctx.send(f"{author.mention} The category '{category_name}' does not exist.")
        return


    existing_channel = discord.utils.get(category.channels, name=channel_name)
    if existing_channel:
        await ctx.send(f"{author.mention} gay nigger agent, you already have a private channel: {existing_channel.mention}")
        return

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        author: discord.PermissionOverwrite(read_messages=True),
        bot.user: discord.PermissionOverwrite(read_messages=True)
    }
    new_channel = await ctx.guild.create_text_channel(channel_name, overwrites=overwrites, category=category, reason="niggermail - privchan")
    await ctx.send(f"{author.mention} fellow gay nigga, a niggermail private corporate distribution channel has been created for you: {new_channel.mention}. happy liberating!")

    await new_channel.edit(slowmode_delay=30)

keep_alive()
bot.run("")

