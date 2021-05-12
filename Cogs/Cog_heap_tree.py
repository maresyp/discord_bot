import binarytree
import discord
from discord.ext import commands
import asyncio
from typing import Optional

from utils.heap_tree import build_max_heap, build_min_heap, build_heap, prepare_response
from utils.utils import make_reply


class HeapTrees(commands.Cog):

    @commands.command(
        name='heap_build_max',
        aliases=['hmax'],
        brief='Build Max Heap Tree',
        help='Build Max Heap Tree\n'
             'Usage: !heap_build_max 1 2 3 4 5'
    )
    async def build_max(self, ctx, *args: Optional[int]):

        response: str = await asyncio.to_thread(prepare_response, list(args), build_max_heap)
        await ctx.reply(make_reply(ctx, response))

    @commands.command(
        name='heap_build_min',
        aliases=['hmin'],
        brief='Build Min Heap Tree',
        help='Build Min Heap Tree\n'
             'Usage: !heap_build_min 1 2 3 4 5'
    )
    async def build_min(self, ctx, *args: Optional[int]):
        response: str = await asyncio.to_thread(prepare_response, list(args), build_min_heap)
        await ctx.reply(make_reply(ctx, response))

    @commands.command(
        name='heap_build',
        aliases=['hbld'],
        brief='Build Heap Tree',
        help='Build Heap Tree\n'
             'Usage: !heap_build 1 2 3 4 5'
    )
    async def build_x(self, ctx, *args: Optional[int]):
        response: str = await asyncio.to_thread(prepare_response, list(args), build_heap)
        await ctx.reply(make_reply(ctx, response))
