import functools
import disnake
from .var import guilds_ids
from .embed_constructor import embed_constructor
from .error import error


def has_perm(admin=None, analyst=None):
    def decorator(func):
        analyst_role = 1313603903186669699 # analyst
        adm_role = 1311466881466765445 # owner hub

        @functools.wraps(func)
        async def wrapper(inter: disnake.ApplicationCommandInteraction, *args, **kwargs):
            self = kwargs.pop('self', None)
            guild = inter.bot.get_guild(guilds_ids[0])
            if not inter.guild:
                return None
            if inter.guild.id not in guilds_ids:
                embed = embed_constructor(title='Ошибка доступа', color='ffffff', image=guild.banner.url)
                embed.description += '**Эта команда доступна только на нашем [официальном сервере](https://discord.gg/sJhvsyQETu)\n\nЗдесь вы можете погрузиться в увлекательный мир RP, создать уникального персонажа, взаимодействовать с другими участниками и развивать свою историю. У нас дружелюбное сообщество, интересные события и захватывающие игровые сценарии.\n\nПрисоединяйтесь и станьте частью этого приключения!**'
                return await inter.response.send_message(embed=embed)
            if analyst or admin:
                if any(role.id == adm_role if admin else analyst_role for role in inter.author.roles) or inter.author.guild_permissions.administrator:
                    if self:
                        return await func(self, inter, *args, **kwargs)
                    return await func(inter, *args, **kwargs)
                else:
                    return await error(inter, "У вас нет прав для использования этой команды.")
            if self:
                return await func(self, inter, *args, **kwargs)
            return await func(inter, *args, **kwargs)
        return wrapper
    return decorator
