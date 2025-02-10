from disnake import TextChannel, Embed, ButtonStyle
from disnake.ui import View, Button
from datetime import datetime


async def log(inter):
    log_chnl: TextChannel = inter.client.get_channel(1268559604116226051)
    msg = await inter.original_response()
    embed = Embed(
        title="Новое действие",
        description=f"**Сервер** - {inter.guild.name}\n"
                    f"**Команда** - {inter.data.name}\n"
                    f"**Выполнил** - {inter.author.mention} (id = {inter.author.id})"
    )
    embed.set_footer(text=datetime.now().strftime("%d.%m.%Y %H:%M"))
    data = inter.data.options
    if data != []:
        embed.description += "\n\n**Аргументы**\n"
        for i in data:
            name = i.name.replace('_', '\\_')
            embed.description += f"{name}: {i.value}\n"
    view = View()
    view.add_item(Button(style=ButtonStyle.url, label="К сообщению", url=msg.jump_url))
    await log_chnl.send(embed=embed, view=view)


