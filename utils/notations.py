import sympy


def is_correct_theta(c1: str, c2: str, n0: int, equation: str) -> dict[str, bool]:
    """
    Check if given c1, c2, n0 are correct answer for given equation\n
    equation should be represented using n symbol\n
    for example n**2 - n + 2
    """
    result: dict[str, bool] = {
        'c1': True,
        'c2': True,
        'n0': True,
        'summary': None
    }
    # prepare equation
    n = sympy.symbols('n')
    equation = equation.replace('^', '**')  # just in case someone used ^ power sign instead of **
    simplified = sympy.simplify(sympy.parsing.parse_expr(f'({equation}) / n**2'))
    # check c2
    result['c2'] = str(sympy.limit_seq(simplified, n)) == c2
    # check n0
    if isinstance(n0, int):
        result['n0'] = n0 >= 1 and sympy.simplify(f"{str(simplified).replace('n', f'{n0}')} > 0")
    else:  # if n0 is not int n0 and c1 are both incorrect
        result['n0'] = False
    # check c1
    if result['n0'] is not False:
        result['c1'] = str(sympy.simplify(f"{str(simplified).replace('n', f'{n0}')}")) == c1
    else:
        result['c1'] = False
    result['summary'] = False not in result.values()

    return result
