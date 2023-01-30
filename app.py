import os
import discord
import leetcode_url
from dotenv import load_dotenv
from threading import Timer

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel
    args = message.content.split(' ')
    if args[0] == '$get':
        if len(args) > 1:
            if args[1] == 'easy':
                question_name, url = leetcode_url.get_problem_url(1)
            elif args[1] == 'medium':
                question_name, url = leetcode_url.get_problem_url(2)
            elif args[1] == 'hard':
                question_name, url = leetcode_url.get_problem_url(3)
            else:
                question_name, url = leetcode_url.get_problem_url(0)

            thread = await channel.create_thread(name='Problem : '+question_name, type=discord.ChannelType.public_thread)
            await thread.send("@everyone")
            await thread.send(url)
            # await channel.send('Problem : '+question_name)
            # await channel.send(url)
        else:
            question_name, url = leetcode_url.get_problem_url(0)
            thread = await channel.create_thread(name='Problem : '+question_name, type=discord.ChannelType.public_thread)
            await thread.send("@everyone")
            await thread.send(url)
            # await channel.send('Problem : '+question_name)
            # await channel.send(url)


# async def create_problem_thread():
#     global timer
#     await client.wait_until_ready()
#     question_name, url = leetcode_url.get_problem_url(0)
#     channel = client.get_channel(int(1013085230283886645))
#     thread  = channel.create_thread(name='Problem : '+question_name, type=discord.ChannelType.public_thread)
#     thread.send('@everyone')
#     thread.send(url)
    # timer.start()


# timer = Timer(30, create_problem_thread)

if __name__ == "__main__":
    #load_dotenv()
    # timer.start()

    # a = create_problem_thread()
    client.run(os.getenv("DISCORD_TOKEN", default=""))

    # timer.cancel()

