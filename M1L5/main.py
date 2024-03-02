import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents) 

@bot.event
async def on_ready():
    print(f"Has iniciado secion como {bot.user}")


@bot.command()
async def mem(ctx):
    with open('M2L1/image/Image1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    

bot.run("MTIwMzM4MjI3OTc0MTc3NTg3Mw.GWR43-.S9l-gEANwe6333esZ_DDhT4lxXl5pdAfWFDtyY")