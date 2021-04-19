from discord.ext import commands

from Cogs.utils import make_reply


class Git(commands.Cog):

    @commands.command(
        name='git',
        brief='Github link for this project',
        help='Usage: !git'
    )
    async def git(self, ctx):
        await ctx.reply(make_reply(ctx, 'https://github.com/maresyp/studia_bot'))