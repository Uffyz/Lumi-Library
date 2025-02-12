from disnake import Embed, Colour

def embed_constructor(title='', description='', color=None, thumbnail=None, footer=None, image=None) -> Embed:
    embed = Embed()
    if title:
        embed.title = title
    if description:
        embed.description = description
    if color:
        if isinstance(color, str):
            embed.colour = int(color, 16)
        else:
            embed.colour = color
    else:
        embed.colour = int('2F3136', 16)
    if thumbnail:
        embed.set_thumbnail(thumbnail)
    if footer:
        embed.set_footer(text=footer)
    if image:
        embed.set_image(image)
    return embed
