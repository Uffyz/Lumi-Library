import disnake
import random
from .values import gifs, scroll_prichuda, scroll_souls, rare_contracts, epic_contracts, legendary_contracts, mythical_contracts, settings
from .emoji import shinystar_emoji, member_emoji, booster_emoji, demons_emoji, mention_emoji, apostle_emoji


async def scrolling(bot, inter, t):
    embed = disnake.Embed(
    )
    embed2 = disnake.Embed(
    )
    penta = bot.get_emoji(1261372055287496866)
    blackstar = bot.get_emoji(1261382383286878311)
    if t == "причуда":
        random_scrolling = random.choice(scroll_prichuda)
        embed.title = f"{shinystar_emoji} \ Прокрутка Причуды!"
        embed.add_field(name=f"{member_emoji} \ Команда выполнена пользователем:", value=inter.author.mention, inline=False)
        embed.add_field(name=f"{booster_emoji} \ Прокручиваем Причуду...", value=disnake.PartialEmoji.from_str(":cyclone:"), inline=False)
        embed.set_image(url=gifs["prichuda"]["scroll"])
        embed2.title = embed.title
        embed2.add_field(name=f"{member_emoji} \ Игрок", value=inter.author.mention, inline=False)
        embed2.add_field(name=f"{shinystar_emoji} \ Поздравляем!", value="Вы получили Причуду!", inline=False)
        embed2.add_field(name=f"", value=f"```Причуда: {random_scrolling}```", inline=False)
        embed2.set_image(url=gifs["prichuda"]["finish"])
    elif t == "душа":
        random_scrolling = random.choice(scroll_souls)
        embed.title = f"{shinystar_emoji} \ Прокрутка Мифической Души"
        embed.add_field(name=f"{member_emoji} \ Команда выполнена пользователем:", value=inter.author.mention, inline=False)
        embed.add_field(name=f"{booster_emoji} \ Прокручиваем Мифическую Душу...", value=disnake.PartialEmoji.from_str(":cyclone:"), inline=False)
        embed.set_image(url=gifs["souls"]["scroll"])
        embed2.title = embed.title
        embed2.add_field(name=f"{member_emoji} \ Игрок", value=inter.author.mention, inline=False)
        embed2.add_field(name=f"{shinystar_emoji} \ Поздравляем!", value="Вы получили Мифическую Душу!", inline=False)
        embed2.add_field(name=f"", value=f"```{random_scrolling}```", inline=False)
        embed2.set_image(url=gifs["souls"]["finish"])
    elif t == "контракт":
        rare_chance = int(settings["rare"])
        epic_chance = int(settings["epic"])
        leg_chance = int(settings["leg"])
        myth_chance = int(settings["myth"])
        chances = [rare_chance, epic_chance, leg_chance, myth_chance]
        first_scrolling = random.choices(["Редкого", "Эпического", "Легендарного", "Мифического"], chances)[0]
        if first_scrolling == "Редкого":
            random_scrolling = random.choice(rare_contracts)
            embed2.set_image(url=gifs["contracts"]["rare"])
            embed2.colour = int("3498DB", 16)
        elif first_scrolling == "Эпического":
            random_scrolling = random.choice(epic_contracts)
            embed2.set_image(url=gifs["contracts"]["epic"])
            embed2.colour = int("9C59B6", 16)
        elif first_scrolling == "Легендарного":
            random_scrolling = random.choice(legendary_contracts)
            embed2.set_image(url=gifs["contracts"]["leg"])
            embed2.colour = int("F1C40F", 16)
        elif first_scrolling == "Мифического":
            random_scrolling = random.choice(mythical_contracts)
            embed2.set_image(url=gifs["contracts"]["myth"])
            embed2.colour = int("992E22", 16)
        embed.title = f"{demons_emoji} \ Прокрутка Контракта"
        embed.add_field(name=f"{mention_emoji} \ Команда выполнена пользователем:", value=inter.author.mention, inline=False)
        embed.add_field(name=f"{booster_emoji} \ Прокручиваем контракт...", value=disnake.PartialEmoji.from_str(":cyclone:"), inline=False)
        embed.set_image(url=gifs["contracts"]["scroll"])
        embed2.title = f"{penta} \ Прокрутка Контракта"
        embed2.add_field(name=f"{blackstar} \ Игрок", value=inter.author.mention, inline=False)
        embed2.add_field(name=f"{apostle_emoji} \ Поздравляем!", value=f"Вы получили Контракт {first_scrolling}-Уровня!", inline=False)
        embed2.add_field(name=f"", value=f"```{random_scrolling}```", inline=False)
    if t != "контракт":
        embed2.colour = disnake.Color.random()
    return embed, embed2