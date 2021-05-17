import asyncio
import binarytree
from discord.ext import commands

from utils.heap_tree import get_properties
from utils.utils import make_reply, parse_optional_int


class BSTTrees(commands.Cog):
    @commands.command(
        name='bst_build',
        aliases=['bstb'],
        brief='Build BST Tree',
        help=f'With this command you can build bst tree\n'
             f'For example:\n'
             f"""
                   ___15______
                  /           \\
                 7         ____30
                / \\       /      \\
               4   13    25       34
              /            \\
             2              27
             \n"""
             f'For this output, input should be:\n'
             f'!bst_build 15 7 30 4 13 25 34 2 None None None None 27 None None\n'
             f'If a node is at index i\n'
             f'left child is always at 2i + 1,\n'
             f'right child at 2i + 2\n'
             f'parent at floor((i - 1) / 2).\n'
             f'"None" indicates absence of a node at that index.\n'
             f'In case of values repeating themselves special syntax with -> operator is supported\n'
             f'None->3 is equivalent to None None None\n'
             f'Above example could be rewritten as:\n'
             f'!bst_build 15 7 30 4 13 25 34 2 None->4 27 None->2\n'
             f'-> Operator can also be used with integer values\n'
             f'For example 5->3 is equivalent to 5 5 5\n'
             f'Another example:\n'
             f"""
                     ______8
                    /       \\
                  3__       10___
                 /   \\           \\
                1     6          _14
                     / \\       /
                    4   7     13
             \n"""
             f'For above output, input should be:\n'
             f'!bst_build 8 3 10 1 6 None 14 None None 4 7 None None 13\n'
             f'Or using -> operator:\n'
             f'!bst_build 8 3 10 1 6 None 14 None->2 4 7 None->2 13'
    )
    async def build_bst(self, ctx, *args):
        def prepare(arr: list[str]) -> str:
            bst_tree = binarytree.build(parse_optional_int(arr))
            return f"From values -> {' '.join((str(_) for _ in bst_tree.values))}\n" \
                   f'{get_properties(bst_tree)}\n' \
                   f"Inorder: {' '.join(str(elem.value) for elem in bst_tree.inorder)}\n" \
                   f"Preorder: {' '.join(str(elem.value) for elem in bst_tree.preorder)}\n" \
                   f"Postorder: {' '.join(str(elem.value) for elem in bst_tree.postorder)}\n" \
                   f'{bst_tree.__str__()}'

        response: str = await asyncio.to_thread(prepare, list(args))
        await ctx.reply(make_reply(ctx, response))

    @commands.command(
        name='bst_insert',
        brief='Insert value to BST Tree [ BETA ]',
        help='Insert value to BST Tree\n'
             'Usage:\n'
             '!bst_insert <value> -> <array representation of bst tree>\n'
             '!bst_insert 10 -> 15 7 30 4 13 25 34 2 None->4 27 None->2'
    )
    async def insert_bst(self, ctx, *args):
        def prepare(arr: list[str]) -> str:
            if arr[1] != '->':
                return "Syntax Error '->' missing, use !help and try again"
            try:
                value = int(arr[0])
            except ValueError:
                return f'{arr[0]} is not convertible to int'
            try:
                bst_tree = binarytree.build(parse_optional_int(arr[2:]))
            except ValueError:
                return "Unable to create bst tree, please check your input\n" \
                       "All values should be convertible to int / None"

            def insert(root: binarytree.Node, val: int) -> str:
                res = ''
                if val == root.value:
                    res += f'Duplicates are not allowed in bst tree !\n' \
                           f'{val} == {root.value}'
                else:
                    if val > root.value:
                        res += f'{val} > {root.value} going right\n'
                        if root.right is None:
                            res += 'None found, inserting value\n'
                            root.right = binarytree.Node(val)
                        else:
                            res += insert(root.right, val)
                    else:
                        res += f'{val} < {root.value} going left\n'
                        if root.left is None:
                            res += 'None found, inserting value\n'
                            root.left = binarytree.Node(val)
                        else:
                            res += insert(root.left, val)
                return res

            return f'{insert(bst_tree, value)}\n' \
                   f'{bst_tree.__str__()}\n' \
                   f"Tree values:\n" \
                   f"{' '.join((str(_) for _ in bst_tree.values))}"

        response: str = await asyncio.to_thread(prepare, list(args))
        await ctx.reply(make_reply(ctx, response))
