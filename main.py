import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

from Cogs.Cog_bst_trees import BSTTrees
from Cogs.Cog_graphs import Graphs
from Cogs.Cog_heap_tree import HeapTrees
from Cogs.Cog_sorting import Sorting
from Cogs.Cog_binary_trees import BinaryTrees
from Cogs.Cog_functions import Functions
from Cogs.Cog_git import Git
from Cogs.Cog_notations import Notations
from Cogs.Cog_rpn import Onp
from Cogs.Cog_math import Math

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN', default=None)
bot = commands.Bot(command_prefix='!')

# Add Cogs here
bot.add_cog(Sorting())
bot.add_cog(Onp())
bot.add_cog(BinaryTrees())
bot.add_cog(Git())
bot.add_cog(Notations())
bot.add_cog(Functions())
bot.add_cog(HeapTrees())
bot.add_cog(BSTTrees())
bot.add_cog(Graphs())
bot.add_cog(Math())


@bot.event
async def on_ready():
    print('Hello, I\'m ready to help you')


@bot.event
async def on_command_error(context: discord.ext.commands.Context, exception: discord.ext.commands):
    if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
        pass


if __name__ == '__main__':
    if TOKEN is not None:
        bot.run(TOKEN)
    else:
        raise Exception('Token not found, unable to run')
