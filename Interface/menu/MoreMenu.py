from disnake import Embed, SelectOption, MessageInteraction
from disnake.ui import Select
from interface.buttons.ButtonRole import ButtonRoles
from interface.embeds import more_embed, roles_embed

class More(Select):
    def __init__(self):
        options = [
            SelectOption(
                label="Описание",
                emoji="<:freeiconinformation4412520:1206172961887883305>",
                description="подробное описание города",
                value="Описание"
            ),
            SelectOption(
                label="Иерархия",
                emoji="<:freeiconhierarchy5584239:1206172964295409694>",
                description="роли города",
                value="Иерархия"
            ),
            SelectOption(
                label="Координаты",
                emoji="<:freeiconequator8048629:1206172958540828722>",
                description="местоположение города",
                value="Координаты"
            )
        ]
        super().__init__(placeholder="Выберите что бы вы хотели узнать?", options=options, custom_id="more_info", min_values=0, max_values=1)
    async def callback(self, inter: MessageInteraction):
        if not inter.values:
            await inter.response.defer()
        if self.values[0] == "Описание":
            await inter.send(embed=more_embed, ephemeral=True)
        elif self.values[0] == "Координаты":
            await inter.send(embed=Embed(description="### Расположение города: `x:?` `y:?` `z:?` ```? ? ?```", color=0xe23639), ephemeral=True)
        elif self.values[0] == "Иерархия":
            await inter.send(embed=roles_embed, ephemeral=True, view=ButtonRoles())