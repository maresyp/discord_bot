from discord.ext import commands
import asyncio

from utils.utils import make_reply


class Graphs(commands.Cog):

    @commands.command(
        name='graph',
        brief='g',
        help='g'
    )
    async def graph_info(self, ctx, user_input: str):
        make_reply(ctx, user_input)
