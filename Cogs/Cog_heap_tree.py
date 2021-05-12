import binarytree
import discord
from discord.ext import commands
import asyncio

from utils.heap_tree import build_max_heap, build_min_heap, build_heap
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
        tree: binarytree.Node = await asyncio.to_thread(build_max_heap, list(args))
        await ctx.reply(make_reply(ctx, tree.__str__()))

    @commands.command(
        name='heap_build_min',
        aliases=['hmin'],
        brief='Build Min Heap Tree',
        help='Build Min Heap Tree\n'
             'Usage: !heap_build_min 1 2 3 4 5'
    )
    async def build_min(self, ctx, *args: int):
        tree: binarytree.Node = await asyncio.to_thread(build_min_heap, list(args))
        await ctx.reply(make_reply(ctx, tree.__str__()))

    @commands.command(
        name='heap_build',
        aliases=['hbld'],
        brief='Build Heap Tree',
        help='Build Heap Tree\n'
             'Usage: !heap_build 1 2 3 4 5'
    )
    async def build_x(self, ctx, *args: int):
        tree: binarytree.Node = await asyncio.to_thread(build_heap, list(args))
        await ctx.reply(make_reply(ctx, tree.__str__()))
