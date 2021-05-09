import binarytree
import heapq


def get_properties(tree: binarytree.Node) -> str:
    if not isinstance(tree, binarytree.Node):
        raise TypeError
    return ''.join((f'{key}: {value}\n' for key, value in tree.properties.items()))


def build_max_heap(arr: list[int]) -> binarytree.Node:
    heapq._heapify_max(arr)
    return binarytree.build(arr)


def build_min_heap(arr: list[int]) -> binarytree.Node:
    heapq.heapify(arr)
    return binarytree.build(arr)

