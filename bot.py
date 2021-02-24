import discord
from random import randint
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

bot = commands.Bot(command_prefix='d!')
bot.debug = False


@bot.event
async def on_ready():
    bot.disabledServers = []
    await bot.change_presence(activity=discord.Game(name="d!help"))


@bot.event
async def on_message(message):
    if(message.author == bot.user):
        return
    if((randint(0, 90) == 1 or bot.debug) and message.guild and not message.content.startswith('d!')):
        msg = await message.reply("You have mail", mention_author=True)
        bot.reactionAuthor = message.author
        await msg.add_reaction('\U0001F4EC')
    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    if(user.id == bot.user.id):
        return
    if(str(reaction) == '\U0001F4EC' and bot.reactionAuthor.id == user.id):
        await user.send("Your mail is: ||DEEZ NUTS||")
        await reaction.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def debug(ctx):
    bot.debug = not bot.debug
    await ctx.send("Debug: "+str(bot.debug))


@bot.command(name="src", brief="Returns link to source code")
async def src(ctx):
    await ctx.send("https://github.com/PopsicleTreehouse/DeezNutsBot")


load_dotenv()
bot.run(getenv('TOKEN'))
