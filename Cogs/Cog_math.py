from discord.ext import commands
import asyncio


class Math(commands.Cog):

    @commands.command(
        name='count_numbers',
        brief='Count Numbers',
        help='Usage:\n'
             '!count_numbers <ile_cyfr> <>'
    )
    async def count_numbers(self, ctx, *args: str):
        pass
