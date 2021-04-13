import discord
from discord.ext import commands


def make_reply(context: discord.ext.commands.Context, command_output: str) -> str:
    """
    Utility to make sending replies easier
    method will use Context.command.brief as default name of command
    Context.command.name will be used as fallback
    :param context: discord Context that caused command
    :param command_output: output of the command that should be sent to user
    :return: str containing message ready to sent to user
    """
    if context.command.brief is not None:
        __command_name = context.command.brief
    else:
        __command_name = context.command.name

    return f"```\n" \
           f'{__command_name}\n' \
           f"{'-' * len(__command_name)}\n" \
           f"{command_output}" \
           f"```"


def check_for_elements(arr: list, required_amount: int):
    """
    Utility to check if user passed enough values for method to run correctly
    :param arr: Check this Array
    :param required_amount: Amount of data required
    :raises ValueError if too few elements are inside arr
    :return: None
    """
    if len(arr) < required_amount: raise ValueError(f'You need to pass at least {required_amount} elements')
