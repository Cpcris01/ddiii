import discord
from discord.ext import commands

description = 'Hola'

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

bot = commands.Bot(command_prefix='$', description=description, intents=intents)    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()#suma
async def add(ctx, one:int, two:int):
     """Adds two numbers together."""
     await ctx.send(one + two)

client.run("MTIwMzM4MjI3OTc0MTc3NTg3Mw.GWR43-.S9l-gEANwe6333esZ_DDhT4lxXl5pdAfWFDtyY")