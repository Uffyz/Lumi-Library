import disnake
from .embed_constructor import embed_constructor

class SendReport(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Тема",
                custom_id="Тема",
                placeholder="Укажите тему вопроса или проблемы.",
                style=disnake.TextInputStyle.short,
                max_length=50
            ),
            disnake.ui.TextInput(
                label="Текст обращения",
                custom_id="Текст обращения",
                placeholder="Чётко и ясно изложите суть вашего вопроса или проблемы.",
                style=disnake.TextInputStyle.long
            )
        ]
        super().__init__(
            title=f"Отправка обращения",
            custom_id="sendreport",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        param = [(key, value) for key, value in inter.text_values.items()]
        embed_success = embed_constructor(title='Обращение принято', description='*Мы рады сообщить, что ваш вопрос был успешно **принят и обработан администратором**. Ваше сообщение было передано, и вы можете ожидать ответа в ближайшее время.*', color='00FF00')
        await inter.send(embed=embed_success, ephemeral=True)
        embed = embed_constructor(title=param[0][1], thumbnail=inter.author.avatar.url, color='1E90FF')
        embed.add_field(name='Текст обращения:', value=param[1][1], inline=False)
        view = disnake.ui.View()
        view.add_item(disnake.ui.Button(label='Ответить', emoji='📨', custom_id=f'reply_report_{inter.author.id}_{param[0][1]}', style=disnake.ButtonStyle.primary))
        chnl = inter.guild.get_channel(1311740856193257474)
        adm_role = inter.guild.get_role(1311297090076282950)
        await chnl.send(content=f'***Уважаемые администраторы,**\n\n Поступил **новый репорт** от {inter.author.mention}. Пожалуйста, проверьте и обработайте его при первой возможности. Спасибо!* 🔔 {adm_role.mention}', embed=embed, view=view)

class ReplyReport(disnake.ui.Modal):
    def __init__(self, target_member, theme):
        self.target_member = target_member
        self.theme = theme
        components = [
            disnake.ui.TextInput(
                label="Ответ на обращение",
                custom_id="Ответ на обращение",
                style=disnake.TextInputStyle.long
            )
        ]
        super().__init__(
            title=f"Ответ на обращение",
            custom_id="sendreport",
            components=components,
        )

    async def callback(self, inter: disnake.ModalInteraction):
        param = [(key, value) for key, value in inter.text_values.items()]

        embed_success = embed_constructor(title='Ответ на обращение', description=f'*Вы успешно ответили на обращение пользователя {self.target_member.mention}.*', color='00FF00')
        await inter.send(embed=embed_success, ephemeral=True)

        view = disnake.ui.View()
        view.add_item(disnake.ui.Button(label='Ответить', emoji='📨', custom_id=f'reply_report_{inter.author.id}', style=disnake.ButtonStyle.primary, disabled=True))
        await inter.message.edit(view=view)

        embed = embed_constructor(title=f'Администратор ответил на ваше обращение "{self.theme}"', color='1E90FF')
        embed.add_field(name='Ответ администратора:', value=param[0][1], inline=False)
        await self.target_member.send(embed=embed)
