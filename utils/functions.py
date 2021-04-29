from functools import cmp_to_key

import sympy


def sort_functions(arr: list[str], min_len: int, max_len: int) -> list[str]:
    """
    Sort functions by asymptotic growth ( Slower goes first )\n
    :param arr: list of functions\n
    :param min_len: min len of arr\n
    :param max_len: max len of arr\n
    :raises ValueError if len is not correct with max / min\n
    :return: sorted arr
    """
    array_len = len(arr)
    if array_len < min_len: raise ValueError('Too few elements passed in array')
    if array_len > max_len: raise ValueError('Too many elements in array')

    n = sympy.symbols('n')
    converted_arr = [sympy.parse_expr(expr.replace('^', '**')) for expr in arr]

    def compare(first: str, second: str):
        limit = str(sympy.limit_seq(sympy.parsing.parse_expr(f'{first} / {second}'), n))
        if limit == 'oo': return 1  # f(x) grows faster
        if limit == '0': return -1  # f(x) grows slower
        if limit == '1': return 0  # both are equal

        # in case limit goes to number
        simplified = sympy.simplify(limit)
        if simplified > 0: return -1
        if simplified < 0: return 1
        return 0

    return [str(elem) for elem in sorted(converted_arr, key=cmp_to_key(compare))]


if __name__ == '__main__':
    print(sympy.parse_expr('adwda'))
    print(sort_functions(['n**2', 'abssss', 'n**3'], 2, 10))
