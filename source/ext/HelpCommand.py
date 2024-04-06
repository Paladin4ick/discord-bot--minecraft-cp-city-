import disnake
from disnake.ext import commands
from interface.embeds import yumiko_embed
from interface.menu.YumikoInfoMenu import YumikoInfoMenu

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="yuimiko", description="Информация о боте [help]")
    async def yumiko(self, inter: disnake.CommandInteraction):
        await inter.send(embed=yumiko_embed, view=disnake.ui.View(timeout=None).add_item(YumikoInfoMenu()))


def setup(bot):
    bot.add_cog(HelpCommand(bot))
