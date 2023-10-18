import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def update_status():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to your mom moan my name"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with your mom"))
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(update_status())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<hello'):
        await message.channel.send('Go fuck yourself!')

with open('fuckYou/token.txt', 'r') as file:
    token = file.read().replace('\n', '')

client.run(token)
