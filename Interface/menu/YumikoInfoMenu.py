import disnake
import datetime

date1 = datetime.datetime(2024, 1, 29, 10, 10, 10)
now = datetime.datetime.today()
yumiko_age = str(now - date1).split(".")[0][:-14]

class YumikoInfoMenu(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(
                label="Кто ты?",
                emoji="<:freeiconquestionmark9797431:1210720549525913670>",
                value="Кто ты?"
            ),
            disnake.SelectOption(
                label="Плюшки для участников",
                emoji="<:freeiconslack3800024:1210720551555960963>",
                value="Плюшки для участников"
            ),
            disnake.SelectOption(
                label="Плюшки для админов",
                emoji="<:freeiconcrown7207192:1210720553350987786>",
                value="Плюшки для админов"
            )
        ]
        super().__init__(placeholder="Что вас интересует?", options=options, custom_id="yu_info", min_values=0, max_values=1)
    async def callback(self, inter: disnake.MessageInteraction):
        if not inter.values:
            await inter.response.defer()
        if self.values[0] == "Кто ты?":
            embed = disnake.Embed()
            embed.description="""
            ### Хочешь узнать кто я?
            ### Я Yumiko - твой помошник и неко-тян бот"""
            embed.add_field(name="Возраст", value=f"`{yumiko_age} дней` ", inline=True)
            embed.add_field(name="Разработчик", value=("<@657323162219839519>"), inline=True)
            embed.add_field(name="Смотрю за", value=f"`{len(inter.guild.members)} участниками`", inline=True)
            embed.add_field(name="Статус", value="`В активной разработке`", inline=True)
            embed.add_field(name="Версия", value="`0.1.9.9`")
            embed.color=0xe23639
            await inter.send(embed=embed)
        
        if self.values[0] == "Плюшки для участников":
            embed = disnake.Embed()
            embed.description="""
            ## Список плюшек для участников и гостей
            ### Развлечение
            - /smile - улыбнуться другому участнику
            - /pinok пнуть участника
            - /punch - ударить участника
            - /hello - отправить гифку с приветствием
            ### Профиль
            - /profile - посмотреть профиль
            - /description - изменить описание профиля
            - /banner - изменить баннер профиля
            - /like - поставить лайк участнику
            - /minecraft - скоро
            \n### В будущем будет больше фишек
            """
            embed.color=0xe23639
            await inter.send(embed=embed)
        
        if self.values[0] == "Плюшки для админов":
            embed = disnake.Embed()
            embed.description="""
            ## Список плюшек для Админов
            - /kick - скоро
            - /ban - скоро
            - <#1218990749018755082> канал с кнопочным созданием новостей
            - /api-role - id роли для вставки в embed
            - /api-channel - id канала для вставки в embed
            - /api-guild - id гильдии для вставки в embed
            - /api-member - id участника для вставки в embed
            """
            embed.color=0xe23639
            await inter.send(embed=embed)