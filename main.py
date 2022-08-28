import os
import discord
import leetcode_url
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    args = message.content.split(' ')
    if args[0] == '$get':
        if len(args) > 1:
            if args[1] == 'easy':
                await message.channel.send(leetcode_url.get_problem_url(1))
            elif args[1] == 'medium':
                await message.channel.send(leetcode_url.get_problem_url(2))
            elif args[1] == 'hard':
                await message.channel.send(leetcode_url.get_problem_url(3))
            else:
                await message.channel.send(leetcode_url.get_problem_url(0))


load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", default="")
client.run(DISCORD_TOKEN)
