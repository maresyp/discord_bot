import sympy


def calculate_theta(equation: str) -> tuple[str, str, str]:
    """
    Calculate c1, c2, n0 for given equation\n
    :param equation: equation\n
    :return: tuple containing c1, c2, n0
    """
    n = sympy.symbols('n')
    equation = equation.replace('^', '**')  # just in case someone used ^ power sign instead of **
    equation = sympy.parse_expr(f'({equation}) / n**2')
    equation = sympy.simplify(equation)
    c2 = sympy.limit_seq(equation, n)
    n0 = None
    # find correct answer by brute force
    for n0 in range(1, 100):
        if sympy.simplify(f"{str(equation).replace('n', f'{n0}')} > 0"):
            break
    c1 = sympy.simplify(f"{str(equation).replace('n', f'{n0}')}")
    return str(c1), str(c2), str(n0)


def is_correct_theta(c1: str, c2: str, n0: int, equation: str) -> tuple[bool, bool, bool]:
    """
    Check if given c1, c2, n0 are correct answer for given equation\n
    equation should be represented using n symbol\n
    for example n**2 - n + 2
    """

    # prepare equation
    n = sympy.symbols('n')
    equation = equation.replace('^', '**')  # just in case someone used ^ power sign instead of **
    simplified = sympy.simplify(sympy.parsing.parse_expr(f'({equation}) / n**2'))
    # check c2
    c2_check = str(sympy.limit_seq(simplified, n)) == c2
    # check n0
    if isinstance(n0, int):
        n0_check = n0 >= 1 and sympy.simplify(f"{str(simplified).replace('n', f'{n0}')} > 0")
    else:  # if n0 is not int ->  n0 and c1 are both incorrect
        n0_check = False
    # check c1
    if n0_check is not False:
        c1_check = str(sympy.simplify(f"{str(simplified).replace('n', f'{n0}')}")) == c1
    else:
        c1_check = False

    return c1_check, c2_check, n0_check
