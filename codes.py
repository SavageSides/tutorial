import discord
from discord.ext import commands

TOKEN = 'NDc5NDg4Mjk5MDM2MzExNTUz.DlZ90w.ni3tO6b9lR7KgGYTN5jlVT1t0Pw'

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('Connected')

client.run(TOKEN)
