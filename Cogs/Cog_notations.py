from discord.ext import commands
import sympy

from utils.utils import make_reply


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
        aliases=['ttc'],
        brief='Theta Check [ BETA ]',
        help=f'Check if c1, c2, n0 are correct for given equation\n'
             f'Note: If you want to calculate correct answer use !theta command instead\n'
             f'Usage: !theta_check <c1> <c1> <n0> <equation>\n'
             f'Usage: !theta_check 1 7 1 2*n**2 - 3*n + 2\n'
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

        result: str = f'{user_input}\n\n' \
                      f"c1 = {c1} -> {'Correct' if str(c1_check) == c1 else 'Wrong'}\n" \
                      f"c2 = {c2} -> {'Correct' if str(c2_check) == c2 else 'Wrong'}\n" \
                      f"n0 = {n0} -> {'Correct' if n0_check else 'Wrong'}\n"

        await ctx.reply(make_reply(ctx, result))

    async def cog_command_error(self, ctx, error):
        print(error)


def is_correct_theta(c1: str, c2: str, n0: int, equation: str) -> dict[str, bool]:
    """
    Check if given c1, c2, n0 are correct answer for given equation\n
    equation should be represented using n symbol\n
    for example n**2 - n + 2
    """
    result: dict[str, bool] = {
        'c1': True,
        'c2': True,
        'n0': True,
        'summary': None
    }
    # prepare equation
    n = sympy.symbols('n')
    equation = equation.replace('^', '**')  # just in case someone used ^ power sign instead of **
    simplified = sympy.simplify(sympy.parsing.parse_expr(f'({equation}) / n**2'))
    # check c2
    result['c2'] = str(sympy.limit_seq(simplified, n)) == c2
    # check n0
    if isinstance(n0, int):
        result['n0'] = n0 >= 1 and sympy.simplify(f"{str(simplified).replace('n', f'{n0}')} > 0")
    else:  # if n0 is not int n0 and c1 are both incorrect
        result['n0'] = False
    # check c1
    if result['n0'] is not False:
        result['c1'] = str(sympy.simplify(f"{str(simplified).replace('n', f'{n0}')}")) == c1
    else:
        result['c1'] = False
    result['summary'] = False not in result.values()

    return result
