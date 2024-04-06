"""Disnake imports"""
import disnake
from disnake.ext import commands

"""Other imports"""
import sqlite3
from loguru import logger
import datetime

"""Create class command [Profile]"""
class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    """View member profile"""
    @commands.slash_command(name="profile", description="Посмотреть профиль участника")
    async def profile(self, inter: disnake.CommandInteraction, member: disnake.Member):
        try:
            time_now = datetime.date.today()
            y = int(member.created_at.strftime("%Y"))
            m = int(member.created_at.strftime("%m"))
            d = int(member.created_at.strftime("%d"))
            created_time = datetime.date(y, m, d)
            discord__reg_time = str(time_now - created_time).split(".")[0][:-14]


            



            y1 = int(member.joined_at.strftime("%Y"))
            m1 = int(member.joined_at.strftime("%m"))
            d1 = int(member.joined_at.strftime("%d"))
            joined_time = datetime.date(y1, m1, d1)
            dicord_joined_time = str(time_now - joined_time).split(".")[0][:-14]

            with sqlite3.connect("./database/users.db") as data:
                c = data.cursor()

                banner = c.execute("SELECT banner FROM users WHERE id={}".format(member.id)).fetchone()[0]
                member_desc = c.execute("SELECT description FROM users WHERE id={}".format(member.id)).fetchone()[0]
                raiting = c.execute("SELECT raiting FROM users WHERE id={}".format(member.id)).fetchone()[0]
                roles = reversed([role for role in member.roles][1::])
                profile_embed = disnake.Embed()
                profile_embed.color=0xe23639
                profile_embed.description=f"""
                    # Профиль {member.display_name}
                    """
                profile_embed.set_thumbnail(member.avatar.url)
                profile_embed.add_field(name="Описание", value=f"```{member_desc}```", inline=False)
                profile_embed.add_field(name="Провел(а) на сервере", value=(f"`{dicord_joined_time} дней`"), inline=True)
                profile_embed.add_field(name="Роли", value=""'\n'.join(role.mention for role in roles), inline=True)
                profile_embed.add_field(name="Рейтинг", value=f"{raiting}", inline=True)
                if banner != "None":
                    profile_embed.set_image(url=banner)


                if int(discord__reg_time) > 365:
                    year1 = f"`{int(discord__reg_time) // 365}-ый(ой) год` "
                    moth1 = f"`{int(discord__reg_time) % 365 // 30} месяц` "
                    day1 = f"`{int(discord__reg_time) % 365 % 30} день` "
                    profile_embed.add_field(name="Пользуется Discord", value=year1 + moth1 + day1, inline=True)

                elif (365 > int(discord__reg_time)) and (int(discord__reg_time) > 30):
                    moth1 = f"`{int(discord__reg_time) % 365 // 30} месяц` "
                    day1 = f"`{int(discord__reg_time) % 365 % 30} день` "
                    profile_embed.add_field(name="Пользуется Discord", value=moth1 + day1, inline=True)
                
                elif 30 > int(discord__reg_time):
                    day1 = f"`{int(discord__reg_time) % 365 % 30} день` "
                    profile_embed.add_field(name="Пользуется Discord", value=day1, inline=True)






                await inter.send(embed=profile_embed)
        except Exception as e:
            logger.error(f"Ошибка выполнения команды, \n<{e}")
            print(e)
        

    """Слеш команды для обновления профиля"""

    """Баннер профиля"""
    @commands.slash_command(name="banner", description="Установить баннер для команды /profile")
    async def banner(self, inter: disnake.CommandInteraction, banner: str):
        if "https://" not in banner:
            await inter.send(embed=disnake.Embed(description="### Укажите прямую ссылку на изображение \nМожете попробовать использовать сервис Postimages", color=0xe23639), ephemeral=True)
        else:
            with sqlite3.connect("./database/users.db") as data:
                c = data.cursor()

                c.execute("UPDATE users SET banner=? WHERE id=?", (banner, inter.author.id))
                await inter.send(embed=disnake.Embed(description="### Баннер успешно обновлен", color=0xe23639), ephemeral=True)
    
    """Описание профиля"""
    @commands.slash_command(name="description", description="Установить описание для команды /profile")
    async def description(self, inter: disnake.CommandInteraction, description = str):
        with sqlite3.connect("./private/users.db") as data:
            c = data.cursor()
            c.execute("UPDATE users SET description=? WHERE id=?", (description, inter.author.id))
            await inter.send(embed=disnake.Embed(description="### Описание успешно обновлено", color=0xe23639), ephemeral=True)

def setup(bot):
    bot.add_cog(Profile(bot))