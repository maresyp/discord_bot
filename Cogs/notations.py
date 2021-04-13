from discord.ext import commands
import sympy


class Notations(commands.Cog):

    @commands.command(
        name='theta',
        brief='Notacja Theta [ coming soon ]',
        help='Usage: !theta n ** 2 + 2 * n'
    )
    async def theta(self, ctx, *args):
        pass
