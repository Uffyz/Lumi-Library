from disnake import Embed, Colour

# import requests
# a = requests.get('https://discord.com/api/v9/invites/lumirp?with_counts=true&with_expiration=true&with_permissions=true')
# print(a.json()['guild']['icon'])

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
        embed.colour = int('ffffff', 16) # 2F3136
    if thumbnail:
        embed.set_thumbnail(thumbnail)
    if footer:
        embed.set_footer(text=footer)
    else:
        embed.set_footer(text='[☁] 𝐋𝐮𝐦𝐢 𝐑𝐨𝐥𝐞 𝐏𝐥𝐚𝐲')
    if image:
        embed.set_image(image)
    return embed
