import binarytree
import heapq
from typing import Callable


def get_properties(tree: binarytree.Node) -> str:
    """
    Get all properties and values of tree in form of str
    """
    if not isinstance(tree, binarytree.Node):
        raise TypeError
    return ''.join((f'{key}: {value}\n' for key, value in tree.properties.items())) \
           + ' '.join((str(_) for _ in tree.values))


def prepare_response(arr: list[int], build_mode: Callable[[list[int]], binarytree.Node]) -> str:
    """
    Generate tree from list representation using build_mode parameter\n
    :param build_mode: Callable that is responsible for creating heap tree\n
    :param arr: list representation of heap tree \n
    :return: str with all of tree properties
    """
    tree: binarytree.Node = build_mode(arr)
    result: str = f"From values -> {' '.join((str(_) for _ in arr))}\n\n" \
                  f"{get_properties(tree)}\n" \
                  f"{tree.__str__()}"
    return result


def build_max_heap(arr: list[int]) -> binarytree.Node:
    """
    Build max heap tree using binarytree.build\n
    :param arr: list to build from\n
    :return: binarytree.Node
    """
    heapq._heapify_max(arr)
    return binarytree.build(arr)


def build_min_heap(arr: list[int]) -> binarytree.Node:
    """
        Build min heap tree using binarytree.build\n
        :param arr: list to build from\n
        :return: binarytree.Node
        """
    heapq.heapify(arr)
    return binarytree.build(arr)


def build_heap(arr: list[int]) -> binarytree.Node:
    """
        Build heap tree using binarytree.build\n
        :param arr: list to build from\n
        :return: binarytree.Node
        """
    return binarytree.build(arr)
