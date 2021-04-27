def bubble_sort(array: list, min_len: int, max_len: int) -> tuple[list, str]:
    """
    Simple bubble sort with steps\n
    :param max_len: max len of array\n
    :param min_len: min len of array\n
    :raises ValueError if len is not correct with max / min\n
    :param array: list that will be sorted\n
    :return: tuple[sorted_list: list, steps: str]
    """
    array_len = len(array)
    if array_len < min_len: raise ValueError('Too few elements passed in array')
    if array_len > max_len: raise ValueError('Too many elements in array')
    steps: str = ''
    changes: bool  # to determine if array is already sorted
    for i in range(array_len):
        changes = False
        steps += ' '.join((str(elem) for elem in array)) + '\n'
        for j in range(0, array_len - i - 1):
            if array[j] > array[j + 1]:
                changes = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if changes is False: break

    return array, steps


def insert_sort(array: list, min_len: int, max_len: int) -> tuple[list, str]:
    """
    Simple insert sort with steps\n
    :param max_len: max len of array\n
    :param min_len: min len of array\n
    :raises ValueError if len is not correct with max / min\n
    :param array: list that will be sorted\n
    :return: tuple[sorted_list: list, steps: str]
    """
    array_len = len(array)
    if array_len < min_len: raise ValueError('Too few elements passed in array')
    if array_len > max_len: raise ValueError('Too many elements in array')
    steps: str = ''
    for i in range(1, array_len):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        steps += ' '.join((str(elem) for elem in array)) + '\n'

    return array, steps


def select_sort(array: list, min_len: int, max_len: int) -> tuple[list, str]:
    """
    Simple select sort with steps\n
    :param max_len: max len of array\n
    :param min_len: min len of array\n
    :raises ValueError if len is not correct with max / min\n
    :param array: list that will be sorted\n
    :return: tuple[sorted_list: list, steps: str]
    """
    array_len = len(array)
    if array_len < min_len: raise ValueError('Too few elements passed in array')
    if array_len > max_len: raise ValueError('Too many elements in array')
    steps: str = ''
    for i in range(array_len):
        steps += ' '.join((str(elem) for elem in array)) + '\n'
        min_id = i
        for j in range(i + 1, array_len):
            if array[min_id] > array[j]:
                min_id = j
        array[i], array[min_id] = array[min_id], array[i]

    return array, steps


def pivot_first(array: list, min_len: int, max_len: int) -> list:
    """
    Pivot for quick sort using first element\n
    :param max_len: max len of array\n
    :param min_len: min len of array\n
    :raises ValueError if len is not correct with max / min\n
    :param array: array after applying algorithm\n
    :return: array: list
    """
    array_len = len(array)
    if array_len < min_len: raise ValueError('Too few elements passed in array')
    if array_len > max_len: raise ValueError('Too many elements in array')
    pivot = array[0]
    i = -1
    j = array_len
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return array
        array[i], array[j] = array[j], array[i]


def pivot_last(array: list, min_len: int, max_len: int) -> list:
    """
    Pivot for quick sort using last element\n
    :param max_len: max len of array\n
    :param min_len: min len of array\n
    :raises ValueError if len is not correct with max / min\n
    :param array: array after applying algorithm\n
    :return: array: list
    """
    array_len = len(array)
    if array_len < min_len: raise ValueError('Too few elements passed in array')
    if array_len > max_len: raise ValueError('Too many elements in array')
    pivot = array[-1]
    i = -1
    for j in range(array_len - 1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[-1] = array[-1], array[i + 1]
    return array
