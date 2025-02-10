from disnake import Embed
from datetime import datetime


class ErrorMessage:
    values = {
        "noid": "Не найдено персонажа с таким ID"
    }


async def error(inter, text):
    if text in ErrorMessage.values:
        text = ErrorMessage.values[text]
    errortext = Embed(
        title="Произошла ошибка",
        description=text,
        color=int("ff0000", 16)
    )
    errortext.set_footer(text=datetime.now().strftime("%d.%m.%Y %H:%M"))
    return await inter.send(embed=errortext)
