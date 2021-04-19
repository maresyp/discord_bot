from discord.ext import commands
import sympy

from Cogs.utils import make_reply


class Notations(commands.Cog):

    @commands.command(
        name='theta',
        aliases=['tt'],
        brief='Notacja Theta [ BETA ]',
        help='Usage: !theta 2*n**2 - 3*n + 2'
    )
    async def theta(self, ctx, *args):
        user_input = ''.join(args)
        n = sympy.symbols('n')
        eq = sympy.parsing.parse_expr(f'({user_input}) / n**2')
        simplified = sympy.simplify(eq)
        c2 = sympy.limit_seq(simplified, n)
        n0 = None

        # find correct answer by brute force
        for n0 in range(1, 100):
            if sympy.simplify(f"{str(simplified).replace('n', f'{n0}')} > 0"):
                break

        c1 = sympy.simplify(f"{str(simplified).replace('n', f'{n0}')}")

        result: str = f'c1 = {c1}, c2 = {c2}, n0 = {n0}'
        await ctx.reply(make_reply(ctx, result))

    @commands.command(
        name='theta_check',
        aliastes=['ttc'],
        brief='Theta Check [ BETA ]',
        help=f'Check if c1, c2, n0 are correct for given equation\n'
             f'Usage: !theta_check'
    )
    async def theta_check(self, ctx, *args):
        pass

    async def cog_command_error(self, ctx, error):
        print(error)
