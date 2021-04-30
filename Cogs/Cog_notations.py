import asyncio

from discord.ext import commands
import sympy

from utils.notations import calculate_theta, is_correct_theta
from utils.utils import make_reply


class Notations(commands.Cog):

    @commands.command(
        name='theta',
        aliases=['tt'],
        brief='Theta Notation',
        help=f'Usage: !theta 2*n**2 - 3*n + 2\n'
             f'Usage: !tt n**2 - 2*n\n'
             f'Or:\n'
             f'Usage: !theta 2*n^2 - 3*n + 2\n'
             f'Usage: !tt n^2 - 2*n\n'
    )
    async def theta(self, ctx, *args):
        user_input: str = ''.join(args)

        result: tuple[str, str, str] = await asyncio.to_thread(calculate_theta, user_input)
        reply = f'c1: {result[0]}, c2: {result[1]}, n0: {result[2]}'
        await ctx.reply(make_reply(ctx, reply))

    @commands.command(
        name='theta_check',
        aliases=['ttc'],
        brief='Theta Check [ BETA ]',
        help=f'Check if c1, c2, n0 are correct for given equation\n'
             f'Note: If you want to calculate correct answer use !theta command instead\n'
             f'Usage: !theta_check <c1> <c1> <n0> <equation>\n'
             f'Usage: !theta_check 1 7 1 2*n**2 - 3*n + 2\n'
    )
    async def theta_check(self, ctx, c1: str, c2: str, n0: int, *args):
        user_input: str = ''.join(args)
        result: tuple[bool, bool, bool] = await asyncio.to_thread(is_correct_theta, c1, c2, n0, user_input)
        reply = f'c1: {result[0]}, c2: {result[1]}, n0: {result[2]}'
        await ctx.reply(make_reply(ctx, reply))

    async def cog_command_error(self, ctx, error):
        print(error)
