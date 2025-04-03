from disnake import Embed, Colour

import requests
# a = requests.get('https://discord.com/api/v9/invites/lumirp?with_counts=true&with_expiration=true&with_permissions=true')
# print(a.json()['guild']['icon'])

def embed_constructor(title='', description='', color=None, thumbnail=None, footer=None, image=None) -> Embed:
    embed = Embed(
        title=title,
        description=description
    )
    url = 'https://cdn.discordapp.com/icons/1119281693262622720/45c0d814dc80ef7d3afd6a16cbf2145b.webp?size=96'
    if color:
        if isinstance(color, str):
            embed.colour = int(color, 16)
        else:
            embed.colour = color
    else:
        embed.colour = int('ffffff', 16) # 2F3136
    if thumbnail:
        embed.set_thumbnail(thumbnail)
    if footer:
        embed.set_footer(text=footer, icon_url=url)
    else:
        embed.set_footer(text='[☁] 𝐋𝐮𝐦𝐢 𝐑𝐨𝐥𝐞 𝐏𝐥𝐚𝐲', icon_url=url)
    if image:
        embed.set_image(image)
    return embed
