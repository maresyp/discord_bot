from discord.ext import commands
import sympy

from Cogs.utils import make_reply


class Notations(commands.Cog):

    @commands.command(
        name='theta',
        aliases=['tt'],
        brief='Notacja Theta [ BETA ]',
        help=f'Usage: !theta 2*n**2 - 3*n + 2\n'
             f'Usage: !tt n**2 - 2*n\n'
             f'Or:\n'
             f'Usage: !theta 2*n^2 - 3*n + 2\n'
             f'Usage: !tt n^2 - 2*n\n'
    )
    async def theta(self, ctx, *args):
        user_input: str = ''.join(args)
        user_input = user_input.replace('^', '**')  # just in case someone used ^ power sign instead of **
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
    async def theta_check(self, ctx, c1: str, c2: str, n0: int, *args):
        user_input: str = ''.join(args)
        user_input = user_input.replace('^', '**')  # just in case someone used ^ power sign instead of **
        print(f'c1 = {c1}, c2 = {c2}, n0 = {n0}, rest = {user_input}\n')  # TODO: DEBUG
        n = sympy.symbols('n')
        simplified = sympy.simplify(sympy.parsing.parse_expr(f'({user_input}) / n**2'))
        c2_check = sympy.limit_seq(simplified, n)
        n0_check = int(n0) >= 1 and sympy.simplify(f"{str(simplified).replace('n', f'{n0}')} > 0")
        c1_check = sympy.simplify(f"{str(simplified).replace('n', f'{n0}')}")
        print(f'c1 = {str(c1_check) == c1}, c2 = {c2_check == c2}, n0 = {n0_check}')  # TODO: DEBUG

        result: str = f'{user_input}\n' \
                      f"c1 = {c1} -> {'Correct' if str(c1_check) == c1 else f'Wrong, should be {c1_check}'}\n" \
                      f"c2 = {c2} -> {'Correct' if str(c2_check) == c2 else f'Wrong, should be {c2_check}'}\n" \
                      f"n0 = {n0} -> {'Correct' if n0_check else 'Wrong'}\n"

        await ctx.reply(make_reply(ctx, result))

    async def cog_command_error(self, ctx, error):
        print(error)
