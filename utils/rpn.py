from dataclasses import dataclass, field


@dataclass
class Stack:
    __stack: list = field(default_factory=list)

    def __str__(self):
        return f"{' '.join((str(x) for x in self.__stack))}"

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def is_empty(self) -> bool:
        return len(self.__stack) == 0

    def peek(self):
        return self.__stack[-1]


def infix_to_postfix(infix_expr: str) -> str:
    """
    :param infix_expr: equation separated by spaces\n
    Example: 2 + 10 * ( 12 - 3 )
    """
    prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    op_stack = Stack([])  # Operand Stack
    postfix = []  # Output

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

            op_stack.pop()  # Drop '(' from stack
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
    return __steps if show_steps else str(operand_stack.pop())


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
