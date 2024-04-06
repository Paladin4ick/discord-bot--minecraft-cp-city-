from disnake.ext.commands import Cog, Bot, slash_command
from disnake import Member, Embed

from utils.config import load_config
import datetime


time = datetime.datetime.now()


class Moderation(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.config = load_config()
    
    @slash_command(name="ban", description="Забанить пользователя")
    async def ban(self, inter, member: Member, *, reason=None):
        author = await inter.guild.get_or_fetch_member(inter.author.id)
        if author.get_role(self.config.adm_role) is None:
            return await inter.send(embed=Embed(description="У вас нет прав данную команду", color=0x2b2d30), ephemeral=True)
        else:
            embed = Embed(description=f"### {member.mention} был забанен по причине: \n### > `{reason}`", color=0x2b2d30)
            embed.set_thumbnail(url=member.avatar)
            embed.set_image(url="https://i.postimg.cc/QxscKPpk/image.png")
            embed.set_author(name=f"{inter.author}", icon_url=inter.author.avatar)
            await inter.send(embed=embed)
            embed = Embed(description="### Вы были забанены на сервере `Fjuiyama` по решению администрации", color=0x2b2d30)
            embed.set_image(url="https://i.postimg.cc/QxscKPpk/image.png")
            await member.send(embed=embed)
            await inter.guild.ban(user=member, reason=reason)

    @slash_command(name="clear", description="Очистить чат")
    async def clear(self, inter, count: int, member: Member = None):
        avatar = inter.author.avatar.url
        channel = inter.guild.get_channel(self.config.logs_channel)
        author = await inter.guild.get_or_fetch_member(inter.author.id)
        if author.get_role(self.config.adm_role) is None:
            return await inter.send(embed=Embed(description="## У вас нет прав на данную команду", color=0x2b2d30), ephemeral=True)

        elif count < 0:
            return await inter.send(embed=Embed(description=f"## Вы не можете удалить `{count}` сообщений", color=0x2b2d30), ephemeral=True)
        
        
        elif member is None:
            delete = await inter.channel.purge(limit=count)
            await inter.send(embed=Embed(description=f"## Очищено `{len(delete)}` сообщений", color=0x2b2d30), ephemeral=True)
            embed = Embed(description=f"## Очистка чата \n### {inter.author.mention} удалил `{len(delete)}` сообщений", timestamp=time, color=0x2b2d30)
            embed.set_thumbnail(url=avatar)
            await channel.send(embed=embed)

        else:
            delete = await inter.channel.purge(limit=count, check=lambda m: m.author==member)
            await inter.send(embed=Embed(description=f"## Очищено `{len(delete)}` сообщений {member}", color=0x2b2d30), ephemeral=True)
            embed = Embed(description=f"## Очистка чата \n### {inter.author.mention} удалил `{len(delete)}` сообщений `{member}`", timestamp=time, color=0x2b2d30)
            embed.set_thumbnail(url=avatar)
            await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Moderation(bot))



    