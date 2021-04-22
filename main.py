import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from Cogs.Sorting import Sorting
from Cogs.binary_trees import BinaryTrees
from Cogs.functions import Functions
from Cogs.git import Git
from Cogs.notations import Notations
from Cogs.onp import Onp

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
