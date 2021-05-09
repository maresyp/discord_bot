import binarytree
import heapq


def get_properties(tree: binarytree.Node) -> str:
    """
    Get all properties of tree in form of str
    """
    if not isinstance(tree, binarytree.Node):
        raise TypeError
    return ''.join((f'{key}: {value}\n' for key, value in tree.properties.items()))


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




