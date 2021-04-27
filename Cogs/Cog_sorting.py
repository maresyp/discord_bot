import asyncio

from discord.ext import commands

from utils.sorting import bubble_sort, insert_sort, select_sort, pivot_first, pivot_last
from utils.utils import make_reply, check_for_elements
from typing import Union

class Sorting(commands.Cog):

    @commands.command(
        name='bubble',
        aliases=['bs'],
        brief='Bubble Sort',
        help='Usage: !bubble 1 2 3 <- All elements are separated by space'
    )
    async def bubble(self, ctx, *args: Union[int, float, complex]):

        # run in separate thread for non blocking io
        result: tuple[list, str] = await asyncio.to_thread(bubble_sort, args, 2, 100)
        await ctx.reply(make_reply(ctx, result[1]))

    @commands.command(
        name='insert',
        brief='Insertion Sort',
        aliases=['is'],
        help='Usage: !insert 1 2 3 <- All elements are separated by space'
    )
    async def insert(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        # run in separate thread for non blocking io
        result: tuple[list, str] = await asyncio.to_thread(insert_sort, __data, 2, 100)
        await ctx.reply(make_reply(ctx, result[1]))

    @commands.command(
        name='select',
        brief='Select sort',
        aliases=['ss'],
        help='Usage: !select 1 2 3 <- All elements are separated by space'
    )
    async def select(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        # run in separate thread for non blocking io
        result: tuple[list, str] = await asyncio.to_thread(select_sort, __data, 2, 100)
        await ctx.reply(make_reply(ctx, result[1]))

    @commands.command(
        name='pivot_first',
        brief='Pivot first element',
        aliases=['pf'],
        help='Usage: !pivot_first 1 2 3 <- All elements are separated by space'
    )
    async def pv_first(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        result: list = await asyncio.to_thread(pivot_first, __data, 2, 100)
        result: str = ' '.join((str(elem) for elem in result))
        await ctx.reply(make_reply(ctx, result))

    @commands.command(
        name='pivot_last',
        brief='Pivot last element',
        aliases=['pl'],
        help='Usage: !pivot_last 1 2 3 <- All elements are separated by space'
    )
    async def pv_last(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        result: list = await asyncio.to_thread(pivot_last, __data, 2, 100)
        result: str = ' '.join((str(elem) for elem in result))
        await ctx.reply(make_reply(ctx, result))

    async def cog_command_error(self, ctx, error):
        print('debug -> ', error)
        if hasattr(error, 'original'):  # Handle other Exceptions

            if isinstance(error.original, ValueError):
                print(error.original)
                await ctx.reply(f'> There is something wrong with your input.\n'
                                f'> Please check usage with !help command and try again')

        else:  # Handle errors that inherit from CommandError

            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.reply(f'> {error}\n'
                                f'> Please check usage with !help command and try again')
