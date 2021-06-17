import binarytree
from discord.ext import commands
import asyncio

from utils.heap_tree import build_max_heap, build_min_heap, build_heap, prepare_response, heap_sort_max_asc
from utils.utils import make_reply


class HeapTrees(commands.Cog):

    @commands.command(
        name='heap_build_max',
        aliases=['hmax'],
        brief='Build Max Heap Tree',
        help='Build Max Heap Tree\n'
             'Usage: !heap_build_max 1 2 3 4 5'
    )
    async def build_max(self, ctx, *args: int):
        response: str = await asyncio.to_thread(prepare_response, list(args), build_max_heap)
        await ctx.reply(make_reply(ctx, response))

    @commands.command(
        name='heap_build_min',
        aliases=['hmin'],
        brief='Build Min Heap Tree',
        help='Build Min Heap Tree\n'
             'Usage: !heap_build_min 1 2 3 4 5'
    )
    async def build_min(self, ctx, *args: int):
        response: str = await asyncio.to_thread(prepare_response, list(args), build_min_heap)
        await ctx.reply(make_reply(ctx, response))

    @commands.command(
        name='heap_build',
        aliases=['hbld'],
        brief='Build Heap Tree',
        help='Build Heap Tree\n'
             'Usage: !heap_build 1 2 3 4 5'
    )
    async def build_x(self, ctx, *args: int):
        def __prepare() -> str:
            tree: binarytree.Node = build_heap(list(args))
            result = f'MAX HEAP: {tree.is_max_heap}\n'
            result += f'MIN HEAP: {tree.is_min_heap}\n'
            result += f'{tree.__str__()}'
            return result
        response: str = await asyncio.to_thread(__prepare)
        await ctx.reply(make_reply(ctx, response))

    @commands.command(
        name="heap_sort_max_asc",
        brief='Max Heap Sort ascending order',
        help='Max Heap Sort ascending order\n'
             'Usage: !heap_sort_max_asc 15 10 13 7 8 9 4 2 1 3'
    )
    async def heap_sort_ma(self, ctx, *args: int):
        response: str = await asyncio.to_thread(heap_sort_max_asc, list(args))
        await ctx.reply(make_reply(ctx, response))

    async def cog_command_error(self, ctx, error):
        print(error)
        # await ctx.reply(f'{error}')
