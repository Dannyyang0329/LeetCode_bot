import random
import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

from leetcode import LeetcodeProblem

class RandomPick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.leetcode_agent = LeetcodeProblem()
        print("Leetcode agent initialized!")

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
    async def get(self, interaction:discord.Interaction, difficulty: Choice[int] = None):
        channel = interaction.channel
        difficulty_value = difficulty.value if difficulty != None else random.randint(1, 3)
        question_name, url = self.leetcode_agent.get_problem_url(difficulty_value)
        # Create a thread with the question name and send the url
        difficulty_text_list = ["RANDOM", "EASY", "MEDIUM", "HARD"]
        assert 0 <= difficulty_value <= 3
        await interaction.response.send_message(f"Creating a thread for problem: {question_name} [{difficulty_text_list[difficulty_value]}]", ephemeral=False)
        # Prepare embed message
        embed=discord.Embed(
            title=question_name,
            url=url,
            description="LeetCode Time: Let's keep the rat race going !\n\nMission accomplished? Time to show off! Post your code in the chat, but shield it with spoiler tags.\n\nNo peeking allowed 🫣",
            color=0x328cec,
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4712/4712104.png")

        thread = await channel.create_thread(name='Problem : '+question_name, type=discord.ChannelType.public_thread)
        await thread.send(embed=embed)
        await thread.send("@everyone")
       

# Cog setup 
async def setup(bot: commands.Bot):
    await bot.add_cog(RandomPick(bot))
