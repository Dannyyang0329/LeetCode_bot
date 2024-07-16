import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

import leetcode_url


class RandomPick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="get", description="Get a random question from leetcode")
    @app_commands.describe(difficulty='What difficulty of question you want to get? (default: random)')
    @app_commands.choices(
        difficulty=[
            Choice(name='easy', value=1),
            Choice(name='medium', value=2),
            Choice(name='hard', value=3),
            Choice(name='random', value=0)
        ]
    )
    async def get(self, interaction:discord.Interaction, difficulty: Choice[int] = 0):
        channel = interaction.channel
        question_name, url = leetcode_url.get_problem_url(difficulty)
        # Create a thread with the question name and send the url
        thread = await channel.create_thread(name='Problem : '+question_name, type=discord.ChannelType.public_thread)
        await thread.send("@everyone")
        await thread.send(url)
       

# Cog setup 
async def setup(bot: commands.Bot):
    await bot.add_cog(RandomPick(bot))
