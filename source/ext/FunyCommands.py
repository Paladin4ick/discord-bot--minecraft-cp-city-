"""Disnake imports"""
import disnake
from disnake.ext import commands

"""Other imports"""
import random
from loguru import logger


"""Create class command [Funy]"""
class Funy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    """command [smile]"""
    @commands.slash_command(name="smile", description="Улыбнуться")
    async def smile(self, inter: disnake.CommandInteraction, member: disnake.Member = None):
        try:
            smile_embed = disnake.Embed()
            smile_embed.set_image(random.choice(smile))
            smile_embed.color=0xe23639
            if member == None:
                await inter.send(f"### {inter.author.display_name} улыбнулся(ась)", embed=smile_embed)
            else:
                await inter.send(f"### {inter.author.display_name} улыбнулся(ась) {member.mention}", embed=smile_embed)
        except Exception as e:
            logger.error(f"Сообщение не было отправленно, ошибка \n{e}")

    """command [punch]"""
    @commands.slash_command(name="punch", description="Ударить участника")
    async def punch(self, inter: disnake.CommandInteraction, member: disnake.Member):
        try:
            punch_embed = disnake.Embed()
            punch_embed.set_image(random.choice(punch))
            punch_embed.color=0xe23639
            await inter.send(f"### {inter.author.display_name} ударил(а) {member.mention}", embed=punch_embed)
        except Exception as e:
            logger.error(f"Сообщение не было отправленно, ошибка \n{e}")

    """command [kick]"""
    @commands.slash_command(name="pinok", description="Пнуть участника")
    async def pinok(self, inter: disnake.CommandInteraction, member: disnake.Member):
        try:
            kick_embed = disnake.Embed()
            kick_embed.set_image(random.choice(kick))
            kick_embed.color=0xe23639
            await inter.send(f"### {inter.author.display_name} пнул(а) {member.mention}", embed=kick_embed)
        except Exception as e:
            logger.error(f"Сообщение не было отправленно, ошибка \n{e}")

    """command [hello]"""
    @commands.slash_command(name="hello", description="Отправить гифку с приветом")
    async def kick(self, inter: disnake.CommandInteraction):
        try:
            hello_embed = disnake.Embed()
            hello_embed.set_image(random.choice(hello))
            hello_embed.color=0xe23639
            await inter.send(f"### {inter.author.display_name} поприветствовал(а) вас", embed=hello_embed)
        except Exception as e:
            logger.error(f"Сообщение не было отправленно, ошибка \n{e}")

def setup(bot):
    bot.add_cog(Funy(bot))