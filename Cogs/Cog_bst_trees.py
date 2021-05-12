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
        help='Help coming soon...'
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
