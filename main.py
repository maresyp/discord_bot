import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from Cogs.Sorting import Sorting
from Cogs.onp import Onp

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN', default=None)
bot = commands.Bot(command_prefix='!')

# Add Cogs here
bot.add_cog(Sorting())
bot.add_cog(Onp())


@bot.event
async def on_command_error(context: discord.ext.commands.Context, exception: discord.ext.commands):

    if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
        pass


bot.run(TOKEN)
