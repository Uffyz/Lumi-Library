import functools
import disnake
from .var import guilds_ids
from .embed_constructor import embed_constructor
from .error import error
from .logging import log


def has_perm(admin=None, analyst=None, rp_curator=None):
    def decorator(func):
        analyst_role = 1313603903186669699 # analyst
        adm_role = 1311466881466765445 # owner hub
        rp_curator_role = 1312118685128855573 # rp curator

        @functools.wraps(func)
        async def wrapper(inter: disnake.ApplicationCommandInteraction, *args, **kwargs):
            anlyst_role = inter.guild.get_role(analyst_role)
            admin_role = inter.guild.get_role(adm_role)
            rp_role = inter.guild.get_role(rp_curator_role)

            self = kwargs.pop('self', None)
            guild = inter.bot.get_guild(guilds_ids[0])
            logscmd = ["выдать", "души", "контракты", "отобрать", "пополнить", "причуда", "char_delete", "char_give", "idchange"
                       'start', 'blacklist', 'claim', 'unclaim']

            if not inter.guild: # Если команда была выполнена не в гильдии
                return None

            if inter.guild.id not in guilds_ids: # Если команда была выполнена не в нужных гильдиях
                if inter.data.name.lower() in logscmd: # Если команда находится в списке чувствительных
                    await log(inter, 'guild')
                embed = embed_constructor(title='Ошибка доступа', color='ffffff', image=guild.banner.url)
                embed.description += '**Эта команда доступна только на нашем [официальном сервере](https://discord.gg/sJhvsyQETu)\n\nЗдесь вы можете погрузиться в увлекательный мир RP, создать уникального персонажа, взаимодействовать с другими участниками и развивать свою историю. У нас дружелюбное сообщество, интересные события и захватывающие игровые сценарии.\n\nПрисоединяйтесь и станьте частью этого приключения!**'
                return await inter.response.send_message(embed=embed)

            if analyst or admin or rp_curator:
                has_access = False
                if admin:
                    if admin_role in inter.author.roles:
                        has_access = True
                elif analyst:
                    if anlyst_role in inter.author.roles:
                        has_access = True
                elif rp_curator:
                    if rp_role in inter.author.roles:
                        has_access = True
                if has_access or inter.author.guild_permissions.administrator:
                    if self:
                        result = await func(self, inter, *args, **kwargs)
                    else:
                        result = await func(inter, *args, **kwargs)
                    if inter.data.name.lower() in logscmd:
                        await log(inter)
                    return result
                else:
                    if inter.data.name.lower() in logscmd:
                        await log(inter, 'perm')
                    return await error(inter, "У вас нет прав для использования этой команды.")
            if self:
                return await func(self, inter, *args, **kwargs)
            return await func(inter, *args, **kwargs)
        return wrapper
    return decorator
