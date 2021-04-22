import matplotlib
import sympy
import discord
from discord.ext import commands
from Cogs.utils import make_reply, check_for_elements
from functools import cmp_to_key
# set backend to non interactive
matplotlib.use('agg')


class Functions(commands.Cog):

    @commands.command(
        name='plot',
        brief='Experimental',
        help='Experimental'
    )
    async def plot(self, ctx, *args):
        user_input: str = ''.join(args)
        user_input = user_input.replace('^', '**')  # just in case someone used ^ power sign instead of **
        user_input: list[str] = user_input.split('&')

        plots: list = []
        for equation in user_input:
            plots.append(sympy.plot(sympy.parsing.parse_expr(equation), autoscale=False, show=False, legend=True))

        main_plot = plots[0]
        if len(plots) > 0:
            plot_colors: list[str] = ['black', 'yellow', 'red', 'orange', 'green']
            for plot in plots[1:]:
                if len(plot_colors) > 0: plot[0].line_color = plot_colors.pop()
                main_plot.append(plot[0])

        main_plot.save('./tmp.png')
        with open('./tmp.png', mode='rb') as file:
            d_file = discord.File(file, filename='./tmp.png')

        def compare(first: str, second: str) -> int:
            pass

        result: str = 'Experimental feature'

        await ctx.reply(make_reply(ctx, result), file=d_file)

    @commands.command(
        name='fsort',
        brief='Sort Functions [ BETA ]',
        help='Sort functions ( slowest goes first ) [ BETA ]\n'
             'To separate functions use &\n'
             'Usage: !fsort n^2 & n^3 \n\n'
             'n!      -> factorial(n)\n'
             'logn    -> log(n)\n'
             'nlogn   -> n*log(n)\n'
             '1       -> n(1)\n'
             'sqrt    -> sqrt(n)\n'
             'n**1.5 <-> n^1.5'
    )
    async def fsort(self, ctx, *args):
        user_input = ''.join(args)
        user_input = user_input.replace('^', '**')  # just in case someone used ^ power sign instead of **
        user_input = user_input.split('&')
        check_for_elements(user_input, 2, 10)
        user_input = [sympy.parsing.parse_expr(expr) for expr in user_input]
        n = sympy.symbols('n')

        def compare(first: str, second: str) -> int:
            lim = str(sympy.limit_seq(sympy.parsing.parse_expr(f'{str(first)} / {str(second)}'), n))
            if lim == 'oo': return 1
            if lim == '0': return -1
            return 0

        user_input.sort(key=cmp_to_key(compare))
        result = '\n'.join((str(eq) for eq in user_input)).replace('**', '^')
        await ctx.reply(make_reply(ctx, result))

    async def cog_command_error(self, ctx, error):
        print(error)


if __name__ == '__main__':
    print(sympy.limit_seq(sympy.parsing.parse_expr('n**2/log(2,n)')))
    print(sympy.parsing.parse_expr('factorial(n)'))