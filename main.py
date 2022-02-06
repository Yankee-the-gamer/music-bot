import discord
from discord import FFmpegPCMAudio
from discord.ext import commands

def get_token():
    with open("token.txt", "r") as token:
        return token.readline()    

class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', help_command=None, description=None)
        self.load_extension("cogs.music")

    async def on_ready(self):
        print(f"logged in as {self.user}")

test = MusicBot()
test.run(get_token())