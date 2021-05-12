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
             f'In general None means that there is no child at this index'
    )
    async def build_bst(self, ctx, *args):
        def prepare(arr: list[str]) -> str:
            bst_tree = binarytree.build(parse_optional_int(arr))
            return f'{get_properties(bst_tree)}\n' \
                   f"Inorder: {' '.join(str(elem.value) for elem in bst_tree.inorder)}\n" \
                   f"Preorder: {' '.join(str(elem.value) for elem in bst_tree.preorder)}\n" \
                   f"Postorder: {' '.join(str(elem.value) for elem in bst_tree.postorder)}\n" \
                   f'{bst_tree.__str__()}'

        response: str = await asyncio.to_thread(prepare, list(args))
        await ctx.reply(make_reply(ctx, response))
