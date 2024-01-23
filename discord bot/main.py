import discord
from bot_logic import gen_pass, flip_a_coin, random_emoji
from settings import settings

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Started as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(settings["command_prefix"]):
        if message.content[1:].startswith('gen_pass'):
            try:
                pass_length = int(message.content.split()[1])
            except IndexError:
                await message.channel.send(f'Specify the password length')
                return
            except ValueError:
                await message.channel.send(f'Input a valid integer')
                return
            pw = gen_pass(pass_length)
            await message.channel.send(f'Length: {len(pw)}      Password: {pw}')
        elif message.content[1:].startswith('flip a coin'):
            await message.channel.send(flip_a_coin)
        elif message.content[1:].startswith('random emoji'):
            await message.channel.send(random_emoji)
        else:
            await message.channel.send(f'Unknown command')

client.run(settings["token"])
