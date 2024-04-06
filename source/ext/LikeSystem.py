"""Disnake imports"""
import disnake
from disnake.ext import commands


"""Other imports"""
from datetime import datetime
from loguru import logger
import sqlite3


"""Create class command [/like]"""
class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    """Send message cooldown command"""
    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        if isinstance(error, commands.CommandOnCooldown):
            retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
            await inter.send(embed=disnake.Embed(description=f"Осталось 0 использований. \n+3 использования через: `{retry_after}`", color=0xe23639))
            logger.warning(f"Не удалось выполнить команду, кулдаун: {retry_after}")



    """slash command [like]"""
    @commands.slash_command(name="like", description="Поставить лайк игроку")
    @commands.cooldown(3, 60*60*24, commands.BucketType.user)
    async def testing(self, inter: disnake.CommandInteraction, member: disnake.Member):
        try:
            with sqlite3.connect("./database/users.db") as data:
                c = data.cursor()
                c.execute("""UPDATE users SET raiting = raiting + 1 WHERE id=?""", (member.id,))
                data.commit()

            await inter.send(embed=disnake.Embed(description=f"{inter.author.display_name}, вы поставили лайк `{member.display_name}`", color=0xe23639))
            logger.success(f"{inter.author.name}, поставил лайк {member}")
        except Exception as e:
            logger.error(f"Ошибка выполнения команды /like \n{e}")


"""Import file in [main.py]"""
def setup(bot):
    bot.add_cog(Testing(bot))