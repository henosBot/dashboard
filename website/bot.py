import discord

intents = discord.Intents.default
intents.members = True
client = discord.Client(
    intents=intents
)

ready = False
@client.event
async def on_ready():
    ready = True

while ready != True:
    pass

bot = client

bot.run('token')