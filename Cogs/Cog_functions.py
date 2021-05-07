import asyncio

import matplotlib
import sympy
import discord
from discord.ext import commands

from utils.functions import sort_functions
from utils.utils import make_reply

# set backend to non interactive
matplotlib.use('agg')


class Functions(commands.Cog):

    @commands.command(
        name='plot',
        brief='Plot Drawing [ BETA ]',
        help='Draw plot of function(s)\n'
             'Usage: !plot n^2 & n**3 and n^4\n'
             'Usage: !plot Abs(sin(x))+5*E^(-x^100)*cos(x)'
    )
    async def plot(self, ctx, *args):
        user_input: str = ''.join(args)
        # just in case someone used ^ power sign instead of ** or 'and' instead of '&'
        user_input = user_input.replace('^', '**').replace('and', '&')
        user_input: list[str] = user_input.split('&')

        plots: list = []
        for equation in user_input:
            plots.append(sympy.plot(sympy.parsing.parse_expr(equation), autoscale=False, show=False, legend=True))

        main_plot = plots[0]
        if len(plots) > 0:
            # TODO: add more colors
            plot_colors: list[str] = ['black', 'yellow', 'red', 'orange', 'green']
            for plot in plots[1:]:
                if len(plot_colors) > 0: plot[0].line_color = plot_colors.pop()
                main_plot.append(plot[0])

        main_plot.save('./tmp.png')
        with open('./tmp.png', mode='rb') as file:
            d_file = discord.File(file, filename='./tmp.png')

        result: str = 'Experimental feature'

        await ctx.reply(make_reply(ctx, result), file=d_file)

    @commands.command(
        name='fsort',
        brief='Sort Functions',
        help='Sort functions ( slowest goes first )\n'
             'To separate functions use "&" or "and"\n'
             'Usage: !fsort n^2 & n^3 \n'
             'Usage: !fsort n^2 and n^3 \n\n'
             'n!      -> factorial(n)\n'
             'logn    -> log(n)\n'
             'nlogn   -> n*log(n)\n'
             '1       -> 1\n'
             'sqrt    -> sqrt(n)\n'
             'n^1.5   -> n^(1/2)'
    )
    async def fsort(self, ctx, *args):
        user_input = ''.join(args)
        user_input = user_input.replace('^', '**').replace('and', '&')
        user_input = user_input.split('&')
        sorted_input: list = await asyncio.to_thread(sort_functions, user_input, 2, 10)

        result: str = '\n'.join(sorted_input).replace('**', '^')
        await ctx.reply(make_reply(ctx, result))

    async def cog_command_error(self, ctx, error):
        print(error)
