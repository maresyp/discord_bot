from discord.ext import commands

from Cogs.utils import make_reply
from utils.stack import Stack


def infix_to_postfix(infix_expr):
    prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    op_stack = Stack([])  # Stos operatorow
    postfix = []  # Wyjscie

    for token in infix_expr.split():
        if len(token) > 1 and token[:1] == '-':
            if '.' in token:
                try:
                    float(token)
                except ValueError:
                    complex(token)
                postfix.append(token)
            elif token[1:].isalnum():
                postfix.append(token)
        elif '.' in token:
            try:
                float(token)
            except ValueError:
                complex(token)
            postfix.append(token)
        elif token.isalnum():
            postfix.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            while op_stack.peek() != '(':
                postfix.append(op_stack.pop())

            op_stack.pop()  # Zrzucenie '(' ze stosu
        else:
            while not op_stack.is_empty() and prec[op_stack.peek()] >= prec[token]:
                postfix.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix.append(op_stack.pop())

    return " ".join(postfix)


def postfix_eval(postfix_expr: str, show_steps: bool = False) -> str:
    __steps: str = ''
    operand_stack = Stack([])
    longest: int = len(max(postfix_expr.split(), key=len))

    for token in postfix_expr.split():
        if token in '+-*/^':
            b = operand_stack.pop()
            a = operand_stack.pop()
            result = do_math(token, a, b)
            operand_stack.push(result)
        else:
            try:
                value = int(token)
            except ValueError:
                try:
                    value = float(token)
                except ValueError:
                    value = complex(token)

            operand_stack.push(value)

        if show_steps: __steps += f"{token}{' ' * (longest - len(token))} | {operand_stack}\n"
    return __steps


def do_math(op, a, b):
    if op == '^':
        return pow(a, b)
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "+":
        return a + b
    else:
        return a - b


class Onp(commands.Cog):

    @commands.command(
        name='onp',
        brief='Odwrócona Notacja Polska',
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
                await ctx.reply(f'> Pamiętaj cholero nie dziel przez zero!.\n'
                                f'> Please check usage with !help command and try again')
