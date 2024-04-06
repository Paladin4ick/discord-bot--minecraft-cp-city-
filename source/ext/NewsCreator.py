from disnake.ext.commands import Cog, slash_command
from disnake import Embed, CommandInteraction, ModalInteraction, TextInputStyle
from utils.config import load_config
from disnake.ui import Modal, TextInput


class NewsMessage(Modal):
    def __init__(self):
        self.config = load_config()

        components = [
            TextInput(
                label="Заголовок",
                custom_id='title',
                min_length=0,
                max_length=256,
                style=TextInputStyle.short
            ),

            TextInput(
                label="Содержание",
                custom_id="description",
                min_length=0,
                max_length=4000,
                style=TextInputStyle.long
            ),
        ]
        super().__init__(title="Fujiyama - News Creator", components=components)
    async def callback(self, interaction: ModalInteraction):
        await interaction.send(embed=Embed(description="### Новость успешно опубликованна", color=0x2b2d30), ephemeral=True)
        role = interaction.guild.get_role(1202846041645383730)
        channel = interaction.guild.get_channel(self.config.news_channel)
        news_embed = Embed()
        news_embed.set_author(name=interaction.author.display_name, icon_url=interaction.author.avatar.url)
        news_embed.color=0x2b2d30
        news_embed.description=f"""
        \n# {interaction.text_values['title']}
        \n{interaction.text_values['description']}"""
        news_embed.set_thumbnail("https://i.postimg.cc/NFydG22n/ava.gif")
        news_embed.set_image("https://i.postimg.cc/KjHBz9h7/image.png")
        await channel.send(f"||{role.mention}||", embed=news_embed)



class NewsCreate(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
    
    @slash_command(name="news", description="Создать сообщение - новость для города")
    async def name(self, inter: CommandInteraction):
        author = await inter.guild.get_or_fetch_member(inter.author.id)
        if author.get_role(self.config.adm_role) is None:
            await inter.send(embed=Embed(description="### Простите, у вас нет прав для этой команды", color=0x2b2d30), ephemeral=True)
        else:
            await inter.response.send_modal(modal=NewsMessage())

    
def setup(bot):
    bot.add_cog(NewsCreate(bot))