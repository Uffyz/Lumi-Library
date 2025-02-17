import disnake
from disnake import TextChannel, ButtonStyle
from disnake.ui import View, Button
from datetime import datetime
from .embed_constructor import embed_constructor


def new_embed(inter, etype):
    embed = embed_constructor(title='Успешное выполнение',
                              description=
                              f'**Сервер** - {inter.guild.name}\n'
                              f'**Команда** - {inter.data.name}\n'
                              f'**Выполнил** - {inter.author.mention} (id = {inter.author.id})\n\n',
                              color=disnake.Colour.brand_green(),
                              footer=datetime.now().strftime('%d.%m.%Y %H:%M'))
    if etype == 'guild':
        embed.title = 'Произошла ошибка'
        embed.description += '**Команда не была выполнена, так как доступна только на основном сервере**\n'
        embed.colour = int('ff0000', 16)
    elif etype == 'perm':
        embed.title = 'Произошла ошибка'
        embed.description += '**Команда не была выполнена, так как у пользователя недостаточно прав**\n'
        embed.colour = int('ff0000', 16)
    if inter.client.application_id == 1262877973539852319:
        embed.description += '**Команда была выполнена на тестовом боте**'
        embed.colour = int('00bfff', 16)
    return embed

async def log(inter, etype='none'):
    log_chnl: TextChannel = inter.client.get_channel(1268559604116226051)
    embed = new_embed(inter, etype)
    view = None
    if etype == 'none':
        msg = await inter.original_response()
        data = inter.data.options
        if data != []:
            embed.description += "\n\n**Аргументы**\n"
            for i in data:
                name = i.name.replace('_', '\\_')
                embed.description += f"{name}: {i.value}\n"
        view = View()
        view.add_item(Button(style=ButtonStyle.url, label="К сообщению", url=msg.jump_url))
    await log_chnl.send(embed=embed, view=view)


