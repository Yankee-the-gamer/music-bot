from discord.ext import commands


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)


def setup(bot):
    bot.add_cog(music(bot))
