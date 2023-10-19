import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        help_command=None
        super().__init__(command_prefix = "?", intents = intents)
        

    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id = 1156650436611289239))
        print(f"Synced slash commands for {self.user}.")
    
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

bot = Bot()

@bot.hybrid_command(name = "test", with_app_command = True, description = "Testing")
@app_commands.guilds(discord.Object(id = 1156650436611289239))
@commands.has_permissions(administrator = True)
async def test(ctx: commands.Context):
    await ctx.defer(ephemeral = True)
    await ctx.reply("hi!")

async def update_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to your mom moan my name"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with your mom"))
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.loop.create_task(update_status())

@bot.command()
async def hello(ctx):
    await ctx.send('Go fuck yourself!')

@bot.command()
async def commands(ctx):
    await ctx.send('The commands available are `hello`, `boo`, `ping`, `hello there`')

@bot.command()
async def ping(ctx):
    if ctx.channel.id == 1156650437005561878:
            await ctx.send(f"Sorry {ctx.author.mention} I can't do that here")
    else:
        counter = 0
        await ctx.send('Why have you done this')
        while counter <= 15:
            await ctx.send(f'{ctx.author.mention} Fuck off!')
            await asyncio.sleep(1)
            counter = counter + 1

@bot.hybrid_command()
async def testing(ctx):
    await ctx.send("This is a hybrid command!")

@bot.hybrid_group(fallback="get")
async def tag(ctx, name):
    await ctx.send(f"Showing tag: {name}")

@tag.command()
async def create(ctx, name):
    await ctx.send(f"Created tag: {name}")

with open('fuckYou/token.txt', 'r') as file:
    token = file.read().replace('\n', '')

bot.run(token)
