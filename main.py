import discord

from discord.ext import commands

class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', help_command=None, description=None)

    async def on_ready(self):
        print(f"logged in as {self.user}")

test = MusicBot()
test.run("")