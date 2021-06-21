from typing import Union


def match_numbers(number: int, divisible: list[Union[tuple[int], int]] = None,
                  not_divisible: list[Union[tuple[int], int]] = None) -> int:
    """
    Determine how many numbers matching given criteria\n
    :param number: power of 10 determining upper limit of digits\n
    for 2 -> 10 - 100\n
    for 3 -> 100 - 1000\n
    :param divisible:\n
    [2, 5] True if checked number is divisible by 2 and 5\n
    [(2, 5)] True if checked numbers either is divisible by 2 or by 5\n
    [(2, 5), 3] True if checked number is either divisible by 2 or 5 and also is divisible by 3\n
    :param not_divisible:\n
    [2, 5] True if checked number is not divisible by 2 and 5\n
    [(2, 5)] True if checked numbers either is not divisible by 2 or by 5\n
    [(2, 5), 3] True if checked number is either not divisible by 2 or 5 and also is not divisible by 3\n
    :return: number of matches
    """
    if number <= 0: raise ValueError('Number must be greater than 1')
    if number > 6: raise ValueError('Too many numbers to check max = 6')
    if divisible is None: divisible = []
    if not_divisible is None: not_divisible = []
    matches: int = 0
    helper: set[bool] = set()
    for num in range(10 ** (number - 1), 10 ** number):
        for div in divisible:
            if isinstance(div, tuple):
                helper.add(any([True for elem in div if num % elem == 0]))
            else:
                helper.add(num % div == 0)
        for n_div in not_divisible:
            if isinstance(n_div, tuple):
                helper.add(any([True for elem in n_div if num % elem != 0]))
            else:
                helper.add(num % n_div != 0)
        if len(helper) == 1 and helper.pop() is True: matches += 1
        helper.clear()
    return matches


if __name__ == '__main__':
    print(match_numbers(2, [(1, 2), 3], [1, 2]))
