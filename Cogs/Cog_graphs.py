from discord.ext import commands
import asyncio
from utils import graphs
from utils.utils import make_reply


class Graphs(commands.Cog):

    @commands.command(
        name='graph',
        brief='g',
        help='g'
    )
    async def graph_info(self, ctx, *args: str):
        def prepare() -> str:
            try:
                g: graphs.Graph = graphs.Graph.from_string(''.join(args))
            except ValueError as e:
                return str(e)
            return g.adjacency_list() + '\n' + g.adjacency_matrix()
        response: str = await asyncio.to_thread(prepare)
        await ctx.reply(make_reply(ctx, response))
