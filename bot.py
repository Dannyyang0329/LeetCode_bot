import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv


# Get token from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", default="")
# Connect to discord
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

# Execute when bot is ready
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"Logged in as {bot.user}")
    print(f"Loaded {len(slash)} commands")


# Load command python files
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} successfully")

# Unload command python files
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension} successfully")

# Reload command python files
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension} successfully")


# Load all python files in cogs directory when bot is ready
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
