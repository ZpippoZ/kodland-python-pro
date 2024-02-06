import discord
from discord.ext import commands
from bot_logic import command_list, gen_pass, flip_a_coin, random_emoji, dec2hex, hex2dec, dec2bin, bin2dec
from settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings["command_prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f'Started as {bot.user}')

@bot.command()
async def list(ctx):
    commands = command_list()
    output='```'
    output+=f'Command prefix: {settings["command_prefix"]}\n'
    output+=f'Command list:\n'
    for i in range(len(commands)):
        output+=f' -{commands[i]}\n'
    output+='```'
    await ctx.send(output)

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

@bot.command()
async def flip_coin(ctx):
    await ctx.send(flip_a_coin())

@bot.command()
async def emoji(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def d2h(ctx, value):
    await ctx.send(dec2hex(value))
    
@bot.command()
async def h2d(ctx, value):
    await ctx.send(hex2dec(value))
    
@bot.command()
async def d2b(ctx, value):
    await ctx.send(dec2bin(value))
    
@bot.command()
async def b2d(ctx, value):
    await ctx.send(bin2dec(value))

bot.run(settings["token"])
