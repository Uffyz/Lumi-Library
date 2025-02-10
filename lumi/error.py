from datetime import datetime
from .embed_constructor import embed_constructor


class ErrorMessage:
    values = {
        "noid": "Не найдено персонажа с таким ID"
    }


async def error(inter, text):
    if text in ErrorMessage.values:
        text = ErrorMessage.values[text]
    errortext = embed_constructor(title='Произошла ошибка', description=text, color='ff0000')
    errortext.set_footer(text=datetime.now().strftime("%d.%m.%Y %H:%M"))
    return await inter.send(embed=errortext)
