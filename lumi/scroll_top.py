import disnake
from .values import gifs
from .emoji import obshiexarki_emoji
from .DB import *
db = DBCommands()


async def scrolltop(num):
    data = await db.top_balance(num)
    embed = disnake.Embed(
        title=f"Лидеры по характеристикам",
        description="",
        colour=int("630215", 16)
    )
    embed.set_footer(text=f"Страница {num+1}")
    datanum = []
    if num == 0:
        numb = num+1
    else:
        numb = num*10+1
    for n in range(len(data)):
        number = data[n][2]
        if number.isdigit():
            result = ""
            length = len(number)
            for i in range(length):
                if i > 0 and (length - i) % 3 == 0 and length > 3:
                    result += ","
                result += number[i]
        else:
            result = number
        datanum.append(result)
    print(data)
    print(datanum)
    if len(data) > 0:
        for k, i in enumerate(data):
            try:
                embed.description = embed.description + f"{k+numb}. ID - **{i[0]}**\nИмя - **{i[1]}**\nХарактеристики - **{datanum[k]}** {obshiexarki_emoji}\n\n"
            except:
                pass
    embed.set_image(url=gifs["leaders"])
    if len(data) >= 10:
        dis = False
    else:
        dis = True
    if num >= 1:
        dis2 = False
    else:
        dis2 = True
    view = disnake.ui.View()
    view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.secondary, custom_id=f"<top_{num}", label="<", disabled=dis2))
    view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.secondary, custom_id=f">top_{num}", label=">", disabled=dis))
    return embed, view
