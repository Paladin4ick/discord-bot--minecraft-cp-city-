from disnake.ext import commands


class AvatarBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            with open("source/materials/avatar.gif", "rb") as avatar:
                await self.bot.user.edit(avatar=avatar.read())
                print("Аватарка бота обновлена")
        except Exception as e:
            print("Аватарка бота не обновлена " + e)


def setup(bot):
    bot.add_cog(AvatarBot(bot))