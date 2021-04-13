from discord.ext import commands
from utils.stack import Stack


def infix_to_postfix(infix_expr):
    prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    op_stack = Stack([]) # Stos operatorow
    postfix = [] # Wyjscie

    for token in infix_expr.split():
        if token.isalnum():
            postfix.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            while op_stack.peek() != '(':
                postfix.append(op_stack.pop())

            op_stack.pop() # Zrzucenie '(' ze stosu
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
            operand_stack.push(int(token))

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
        await ctx.reply(f"```"
                        f'Odwrócona Notacja Polska    \n'
                        f'------------------------    \n'
                        f'[Input]: {__input}          \n'
                        f'------------------------    \n'
                        f'{infix_to_postfix(__input)} \n'
                        f'------------------------    \n'
                        f'{postfix_eval(infix_to_postfix(__input), show_steps=True)}'
                        f"```")

    async def cog_command_error(self, ctx, error):
        print('debug -> ', error)
        if hasattr(error, 'original'):  # Handle other Exceptions

            if isinstance(error.original, ValueError):
                await ctx.reply(f'> {error.original}\n'
                                f'> Please check usage with !help command and try again')