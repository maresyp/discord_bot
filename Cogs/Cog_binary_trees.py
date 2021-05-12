from discord.ext import commands
import binarytree

from utils.utils import make_reply


class BinaryTrees(commands.Cog):

    @commands.command(
        name='binary_tree',
        aliases=['bt'],
        brief='Simple Binary Tree',
        help='Usage: !binary_tree'
    )
    async def binary_tree(self, ctx):
        await ctx.reply(make_reply(ctx, str(binarytree.tree(height=3, is_perfect=False))))

    @commands.command(
        name='heap_tree',
        aliases=['ht'],
        brief='Simple Heap Tree ( max )',
        help='Usage: !heap_tree'
    )
    async def heap_tree(self, ctx):
        await ctx.reply(make_reply(ctx, str(binarytree.heap(height=3, is_perfect=False))))

    @commands.command(
        name='bst_tree',
        aliases=['bst'],
        brief='Simple BST Tree',
        help='Usage: !bst_tree'
    )
    async def bst_tree(self, ctx):
        await ctx.reply(make_reply(ctx, str(binarytree.bst(height=3, is_perfect=False))))


if __name__ == '__main__':
    # Generate a random binary tree and return its root node.
    my_tree = binarytree.tree(height=3, is_perfect=False)

    # Generate a random BST and return its root node.
    my_bst = binarytree.bst(height=3, is_perfect=True)

    # Generate a random max heap and return its root node.
    my_heap = binarytree.heap(height=3, is_max=True, is_perfect=False)
