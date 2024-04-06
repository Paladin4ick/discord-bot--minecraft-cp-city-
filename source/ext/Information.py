"""Disnake imports"""
import disnake
from disnake.ext import commands
from disnake.ui.view import View

"""File imports"""
from utils.config import load_config
from interface.embeds import info_embed, rules_embed
from interface.menu.MoreMenu import More

"""Other imports"""
import datetime

"""Create class [Anketa]"""
class Anketa(disnake.ui.Modal):
    def __init__(self):
        self.config = load_config()


        components = [

            disnake.ui.TextInput(
                label="Никнейм",
                placeholder="Введите свой ник Minecraft",
                custom_id="enter_nick"
                ),
            disnake.ui.TextInput(
                label="Возраст",
                placeholder="Введите свой реальный возраст",
                custom_id="enter_age"
                ),
            disnake.ui.TextInput(
                label="Умения",
                placeholder="Укажите что вы умеете делать лучше всего в Minecraft",
                custom_id="enter_skills",
                ),
            disnake.ui.TextInput(
                label="Причина / почему именно вы",
                placeholder="Укажите причину вступления и почему мы должны взять именно вас",
                custom_id="enter_reason",
                style=disnake.TextInputStyle.long
                )
            ]
        super().__init__(title="Заявка в город", components=components)

    """Send user anketa in [qts] channel""" 
    async def callback(self, interaction: disnake.ModalInteraction):
        
        global member_name
        member_name = interaction.text_values['enter_nick']

        channel = interaction.guild.get_channel(self.config.qts_channel)
        await interaction.send(embed=disnake.Embed(description="### Ваша заявка успешно отправлена", color=0xe23639), ephemeral=True)

        global anketa_message
        anketa_embed = disnake.Embed(color=0xe23639, description=f"""
        # Заявка {interaction.author}
        \n### Ник ```{interaction.text_values["enter_nick"]}```
        \n### Возраст ```{interaction.text_values["enter_age"]}```
        \n### Умения ```{interaction.text_values["enter_skills"]}```
        \n### Причина вступления / почему должны принять ```{interaction.text_values["enter_reason"]}```
        """, timestamp=datetime.datetime.now()).set_image("https://i.postimg.cc/XqYR6bdY/image.png")
        anketa_message = await channel.send(embed=anketa_embed, view=AcceptExileButton())

"""Create class [AcExButton]"""
class AcceptExileButton(View):
    def __init__(self):
        self.config = load_config()
        super().__init__(timeout=None)
    
    """Accept button"""
    @disnake.ui.button(label="Принять в город", style=disnake.ButtonStyle.green, custom_id="accept_anketa")
    async def accept(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        accept_embed = disnake.Embed(description="""
        ### Привет, твоя заявка в город принята, добро пожаловать в [Fujiyama](https://discord.com/channels/1202846041645383730/1202846043310526508)
        """, color=0x2b2d30).set_image("https://i.postimg.cc/brYHqJZt/image.png")
        await member_anketa.send(embed=accept_embed)
        await member_anketa.add_roles(inter.guild.get_role(self.config.member_role))
        await anketa_message.edit(view=None)
        await inter.send(embed=disnake.Embed(description="Заявка принята", color=0xe23639))
        await member_anketa.edit(nick=member_name)

    """Exile button"""
    @disnake.ui.button(label="Отказать", style=disnake.ButtonStyle.red, custom_id="exile")
    async def exile(self, buttton: disnake.ui.button, inter: disnake.MessageInteraction):
        exile_embed = disnake.Embed(description="""
        ### Привет, к сожеланию твоя заявка отклонена. Если хочешь, позже попробуй еще раз
        """, color=0xe23639).set_image("https://i.postimg.cc/MHs0HSBr/image.png")
        await member_anketa.send(embed=exile_embed)
        await anketa_message.edit(view=None)
        await inter.send(embed=disnake.Embed(description="Туда его нахуй", color=0xe23639))


"""Create class button [more_info]"""
class ButtonInfo(View):
    def __init__(self):
        self.config = load_config()
        super().__init__(timeout=None)

    """Buttons more info"""
    @disnake.ui.button(label="Подробнее", style=disnake.ButtonStyle.blurple, custom_id="more", emoji="<:freeiconbooks167756:1205888531063640175>")
    async def more(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        view = View(timeout=None)
        view.add_item(More())
        await inter.send(ephemeral=True, view=view)

    """Button rules"""
    @disnake.ui.button(label="Правила", style=disnake.ButtonStyle.red, custom_id="rules", emoji="<:freeiconrules7180074:1205888535480242300>")
    async def rules(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        await inter.send(embed=rules_embed, ephemeral=True)

    """Button join city"""
    @disnake.ui.button(label="Вступить в город", style=disnake.ButtonStyle.green, custom_id="anketa", emoji="<:freeiconchecklist4151025:1205888533395537960>")
    async def anketa(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        if inter.author.get_role(self.config.member_role) is None:
            global member_anketa
            member_anketa = inter.author
            modal=Anketa()
            await inter.response.send_modal(modal=modal)
        else:
            await inter.send(embed=disnake.Embed(description="### Вы уже состоите в `Fujiyama`", color=0xe23639), ephemeral=True)
    
    @disnake.ui.button(label="Стать гостем нашего города", style=disnake.ButtonStyle.gray, custom_id="quest", emoji="<:1130090848466513980:1218997447183958107>", row=1)
    async def quest(self, button: disnake.ui.button, inter: disnake.MessageInteraction):
        role = inter.guild.get_role(self.config.quest_role)
        if inter.author.get_role(self.config.quest_role) is None:
            await inter.author.add_roles(role)
            await inter.send(embed=disnake.Embed(description="### Поздравляем, вы стали нашим гостем", color=0xe23639), ephemeral=True)
        else:
            await inter.send(embed=disnake.Embed(description="### Вы уже являетесь нашим гостем", color=0xe23639), ephemeral=True)
    @disnake.ui.button(label="Paladin4ick", style=disnake.ButtonStyle.link, url="https://bento.me/paladin4ick", emoji="<:freeiconlink1925558:1205890874085474364>", row=1,)
    async def url(self, button: disnake.ui.button):
        ...

"""Create calss info message"""
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()
        self.persistent_views_added = False
    
    @commands.command()
    @commands.has_any_role(1219004615966720210)
    async def info(self, inter: disnake.CommandInteraction):
        await inter.send(embed=info_embed, view=ButtonInfo())
    
    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistent_views_added:
            return
        self.bot.add_view(ButtonInfo(), message_id=(1219009919114809456))
    
def setup(bot):
    bot.add_cog(Info(bot))
