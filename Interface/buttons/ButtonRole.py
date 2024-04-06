import disnake
from disnake.ui import button
from disnake.ui.view import View

from utils.config import load_config

class ButtonRoles(View):
    def __init__(self):
        self.config = load_config()
        super().__init__(timeout=None)
                        
    @button(label="Оповещения `Yumiko`", style=disnake.ButtonStyle.blurple, custom_id="yumiko_ping", emoji="<:freeiconrobot630426:1205890872332521482>")
    async def ping_yuimiko(self, button: button, inter: disnake.MessageInteraction):
        if inter.author.get_role(self.config.ping_role) is None:
            await inter.author.add_roles(inter.guild.get_role(self.config.ping_role))
            await inter.send(embed=disnake.Embed(description="### Оповещения об обновлениях бота включены", color=0x2b2d30), ephemeral=True)
        else:
            await inter.author.remove_roles(inter.guild.get_role(self.config.ping_role))
            await inter.send(embed=disnake.Embed(description="### Оповещения об обновлениях бота выключены", color=0x2b2d30), ephemeral=True)

    @button(label="Paladin4ick", style=disnake.ButtonStyle.link, emoji="<:freeiconlink1925558:1205890874085474364>", url="https://bento.me/paladin4ick")
    async def link(self, button: button, inter: disnake.MessageInteraction):
        pass

from disnake.ext import commands

"""Класс с кнопками"""
class Butto(disnake.ui.view.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    """1 кнопка"""
    @disnake.ui.button(label="1", style=disnake.ButtonStyle.blurple, custom_id="b")
    async def button1(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        ...
    
    """2 кнопка"""
    @disnake.ui.button(label="2", style=disnake.ButtonStyle.gray, custom_id="bb")
    async def button1(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        ...
    
    """3 кнопка"""
    @disnake.ui.button(label="3", style=disnake.ButtonStyle.green, custom_id="bbb")
    async def button1(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        ...
    
    """И т.д."""

class TEST(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="test", description="test buttons")
    async def test(self, inter: disnake.CommandInteraction):
        inter.send(embed=disnake.Embed(description="# TEST"), view=Butto())

    