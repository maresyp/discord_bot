import discord
from discord.ext import commands


class HeapTrees(commands.Cog):

    @commands.command(
        name='heap_build_max',
        aliases=['hmax'],
        brief='Heap Max',
        help='Usage: !heap_build_max 1 2 3 4 5'
    )
    def build_max(self, ctx):
        pass

    @commands.command(
        name='heap_build_min',
        aliases=['hmin'],
        brief='Heap Min',
        help='Usage: !heap_build_min 1 2 3 4 5'
    )
    def build_max(self, ctx):
        pass

    @commands.command(
        name='heap_build',
        aliases=['hbld'],
        brief='Heap',
        help='Usage: !heap_build 1 2 3 4 5'
    )
    def build_max(self, ctx):
        pass

