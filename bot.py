import discord
import os # default module
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv() # load all the variables from the env file
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.load_extension("cogs.greetings")
bot.run(os.getenv('TOKEN')) # run the bot with the token
