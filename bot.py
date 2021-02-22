import discord
from random import randint
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from time import sleep

bot = commands.Bot(command_prefix='d!')
client = discord.Client()


@bot.event
async def on_ready():
    bot.disabledServers = []
    await bot.change_presence(activity=discord.Game(name="d!help"))


@bot.event
async def on_message(message):
    if(message.author == bot.user):
        return
    if(randint(0, 900) == 1):
        bot.msg = await message.reply("You have mail", mention_author=True)
        bot.reactionAuthor = message.author
        await bot.msg.add_reaction('\U0001F4EC')
    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    if(user.id == bot.user.id):
        return
    if(str(reaction) == '\U0001F4EC' and bot.reactionAuthor.id == user.id):
        await user.send("Your mail is: ||DEEZ NUTS||")
        await bot.msg.delete()

load_dotenv()
bot.run(getenv('TOKEN'))
