from discord.ext import commands

from utils.rpn import infix_to_postfix, postfix_eval
from utils.utils import make_reply


class Onp(commands.Cog):

    @commands.command(
        name='onp',
        aliases=['rpn'],
        brief='Reverse Polish Notation',
        help='Usage: !onp ( ( 2 + 7 ) / 3 + ( 14 - 3 ) * 4 ) / 2 <- All elements are separated by space'
    )
    async def onp(self, ctx, *args):

        __input: str = ' '.join((str(_) for _ in args))
        if len(__input) <= 0: raise ValueError('Not enough args passed')

        output: str = f'[Input]: {__input}          \n' \
                      f'------------------------    \n' \
                      f'{infix_to_postfix(__input)} \n' \
                      f'------------------------    \n' \
                      f'{postfix_eval(infix_to_postfix(__input), show_steps=True)}'

        await ctx.reply(make_reply(ctx, output))

    async def cog_command_error(self, ctx, error):
        print('debug -> ', error)
        if hasattr(error, 'original'):  # Handle other Exceptions
            print(error.original)  # print error to console

            if isinstance(error.original, ValueError):
                await ctx.reply(f'> There is something wrong with your input.\n'
                                f'> Please check usage with !help command and try again')

            if isinstance(error.original, ZeroDivisionError):
                await ctx.reply(f'> Zero Division!.\n'
                                f'> Please check usage with !help command and try again')
