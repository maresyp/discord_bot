from discord.ext import commands


class Onp(commands.Cog):

    @commands.command(
        name='onp',
        brief='Odwrócona Notacja Polska [ coming soon ]',
        help='Tutaj wiecej pomocy'
    )
    async def onp(self, ctx, *args):
        print(ctx)
        await ctx.reply(f'Odwrócona Notacja Polska \n'
                        f'------------------------ \n'
                        f'[Input]: {args}      \n'
                        f'------------------------ \n'
                        f'')
