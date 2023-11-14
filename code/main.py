import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import random

#token to run, pulls token from external txt for security
try:
    with open('security/token.txt', 'r') as file:
        token = file.read().replace('\n', '')
except OSError:
    print("Could not find token.txt, please create it in the security folder and place your bot token inside.")
    exit()
else:
    print("Token loaded successfully.")

#guild ID to run, pulls token from external txt for security
try:
    with open('security/guild.txt', 'r') as file:
        guildID = file.read().replace('\n', '')
except OSError:
    print("Could not find guild.txt, please create it in the security folder and place your guild ID inside.")
    exit()
else:
    print("Guild ID loaded successfully.")

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix = ">", intents = intents)
        
    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id = guildID))
        print(f"Synced slash commands for {self.user}.")
    
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

bot = Bot()

@bot.hybrid_command(name = "test", with_app_command = True, description = "Testing")
@app_commands.guilds(discord.Object(id = guildID))
@commands.has_permissions(administrator = True)
async def test(ctx: commands.Context):
    await ctx.defer(ephemeral = True)
    await ctx.reply("hi!")

@bot.hybrid_command(name = "sup", with_app_command = True, description = "Prompts a response")
@app_commands.guilds(discord.Object(id = guildID))
@commands.has_permissions(administrator = False)
async def sup(ctx: commands.Context):
    await ctx.defer(ephemeral = True)
    await ctx.reply("What do you want you prick?")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.loop.create_task(update_status())

@bot.command()
async def hello(ctx):
    await ctx.send('Go fuck yourself!')

@bot.command()
async def boo(ctx):
    await ctx.send('Your mom is a fucking whore!')

@bot.command()
async def hellothere(ctx):
    await ctx.send('General Kenobi you fool \nhttps://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326')

@bot.command()
async def ping(ctx):
    if ctx.channel.id == 1156650437005561878:
            await ctx.send(f"Sorry {ctx.author.mention} I can't do that here")
    else:
        counter = 0
        await ctx.send('Why have you done this')
        while counter <= 15:
            if random.random() < 0.05:
                await ctx.send(f'{ctx.author.mention} I love you!')
            else:
                await ctx.send(f'{ctx.author.mention} Fuck off!')
            await asyncio.sleep(1)
            counter = counter + 1

@bot.hybrid_command(fallback="freddy")
async def freddy(ctx):
    await ctx.send(f"Oh hi {ctx.author.global_name}\nAre you talking about the famous Freddy Fazbear?\nIn the eerie realm of animatronic entertainment, there exists a notorious establishment known as Freddy Fazbear's Pizza. Founded in the 1980s, this seemingly innocent family-friendly restaurant quickly gained a dark reputation that would echo through the years. The story behind Freddy Fazbear is one of mystery, horror, and the haunting legacy of animatronic characters.\nFreddy Fazbear, the titular character, is an anthropomorphic brown bear adorned with a bowtie and a top hat. Alongside his animatronic companions — Bonnie the Bunny, Chica the Chicken, and Foxy the Pirate Fox — Freddy graced the stage at the pizza joint, entertaining children and families with lively performances and catchy tunes. However, behind the cheerful facade lurked a grim and disturbing history.")
    await ctx.send(f"As the legend goes, a series of unfortunate incidents unfolded at Freddy Fazbear's Pizza. Tales of missing children and mysterious disappearances began to circulate, shrouding the establishment in an aura of dread. Rumors of a malevolent force possessing the animatronics and a sinister connection between the characters and the missing children began to surface.\nThe lore deepens with the introduction of the enigmatic Purple Guy, a shadowy figure connected to the dark events at Freddy Fazbear's Pizza. It is revealed that the Purple Guy, whose true identity remains obscured, was responsible for a string of heinous acts, including the dismantling and repurposing of animatronic characters. This malevolent force added an element of psychological horror to the lore, as players and enthusiasts delved into the mysteries surrounding Freddy Fazbear's past.\nThe backstory further unfolds in various iterations of the Five Nights at Freddy's game series, each installment peeling back layers of the chilling narrative. The lore incorporates elements of paranormal activity, supernatural occurrences, and the haunting afterlife of the animatronics. The concept of 'The Bite of '87', a gruesome incident where an animatronic character supposedly attacked a human, adds another layer of horror to the Freddy Fazbear saga.\nDespite the unsettling history, Freddy Fazbears Pizza endures in the hearts and nightmares of those who dare to explore its lore. The iconic characters, the haunting atmosphere, and the enigmatic Purple Guy have cemented Freddy Fazbear as a symbol of the darker side of animatronic entertainment, captivating fans with a tale that transcends the boundaries between fiction and fear.")

@bot.hybrid_command()
async def testing(ctx):
    await ctx.send("This is a hybrid command!")

@bot.hybrid_group(fallback="get")
async def tag(ctx, name):
    await ctx.send(f"Showing tag: {name}")

@tag.command()
async def create(ctx, name):
    await ctx.send(f"Created tag: {name}")

#status upater for rolling status
async def update_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you fumble that girl"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to your mom moan my name"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with your mom"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="siege for your mom's love"))
        await asyncio.sleep(5)

bot.run(token)
