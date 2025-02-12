from disnake import Embed, Colour

def embed_constructor(title='', description='', color=None, thumbnail=None, footer=None, image=None) -> Embed:
    embed = Embed(
        title=title,
        description=description
    )
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
    else:
        embed.set_footer(text='[☁] 𝐋𝐮𝐦𝐢 𝐑𝐨𝐥𝐞 𝐏𝐥𝐚𝐲', icon_url='https://cdn.discordapp.com/icons/1119281693262622720/e50b732ea840bfc2b15875da678d0083.webp?size=96')
    if image:
        embed.set_image(image)
    return embed
