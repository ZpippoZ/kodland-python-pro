import discord
from discord.ext import commands
from bot_logic import gen_pass, flip_a_coin, random_emoji
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings["command_prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f'Started as {bot.user}')

@bot.command()
async def password(ctx, pass_length):
    try:
        pass_length = int(pass_length)
    except ValueError:
        await ctx.send("Input a valid integer")
        return
    if pass_length < 1:
        await ctx.send("Input an integer greater than 0")
    await ctx.send(gen_pass(pass_length))

bot.run(settings["token"])
