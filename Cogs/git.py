import discord
from discord.ext import commands

from Cogs.utils import make_reply


class Git(commands.Cog):

    @commands.command(
        name='git',
        brief='Github link for this project',
        help='Usage: !git'
    )
    async def git(self, ctx):
        embed = discord.Embed()
        embed.description = f'Github link for this project:\n' \
                            f'-------------------------------\n' \
                            f'https://github.com/maresyp/studia_bot'
        await ctx.reply(embed=embed)
