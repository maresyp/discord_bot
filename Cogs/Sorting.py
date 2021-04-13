from discord.ext import commands
from Cogs.utils import make_reply, check_for_elements


class Sorting(commands.Cog):

    @commands.command(
        name='bubble',
        aliases=['bs'],
        brief='Bubble Sort',
        help='Usage: !bubble 1 2 3 <- All elements are separated by space'
    )
    async def bubble(self, ctx, *args):
        __data: list = []
        for elem in args:
            __data.append(int(elem))

        check_for_elements(__data, 2)

        __steps: str = ''
        n = len(__data)
        for i in range(n - 1):  # should be n-1
            for j in range(0, n - i - 1):
                if __data[j] > __data[j + 1]:
                    __data[j], __data[j + 1] = __data[j + 1], __data[j]
            __steps += ' '.join((str(elem) for elem in __data)) + '\n'

        await ctx.reply(make_reply(ctx, __steps))

    @commands.command(
        name='insert',
        brief='Insertion Sort',
        aliases=['is'],
        help='Usage: !insert 1 2 3 <- All elements are separated by space'
    )
    async def insert(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        check_for_elements(__data, 2)

        def __insertion_sort(arr: list[int]) -> str:
            __steps: str = ''
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                __steps += ' '.join((str(_) for _ in __data)) + '\n'
            return __steps

        await ctx.reply(make_reply(ctx, __insertion_sort(__data)))

    @commands.command(
        name='select',
        brief='Select sort',
        aliases=['ss'],
        help='Usage: !select 1 2 3 <- All elements are separated by space'
    )
    async def select(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        check_for_elements(__data, 2)

        def __select_sort(A: list):
            __steps: str = ''
            for i in range(len(A)):
                __steps += ' '.join((str(_) for _ in __data)) + '\n'
                min_idx = i
                for j in range(i + 1, len(A)):
                    if A[min_idx] > A[j]:
                        min_idx = j
                A[i], A[min_idx] = A[min_idx], A[i]
            return __steps

        await ctx.reply(make_reply(ctx, __select_sort(__data)))

    @commands.command(
        name='pivot_first',
        brief='Pivot first element',
        aliases=['pf'],
        help='Usage: !pivot_first 1 2 3 <- All elements are separated by space'
    )
    async def pivot_first(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        check_for_elements(__data, 2)

        def __low_partition(arr: list, low: int, high: int) -> str:
            __result = ''
            pivot = arr[low]
            i = low - 1
            j = high + 1

            while True:
                i += 1
                while arr[i] < pivot:
                    i += 1
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    __result = ' '.join((str(_) for _ in arr))
                    return __result
                arr[i], arr[j] = arr[j], arr[i]

        await ctx.reply(make_reply(ctx, __low_partition(__data, 0, len(__data) - 1)))

    @commands.command(
        name='pivot_last',
        brief='Pivot last element',
        aliases=['pl'],
        help='Usage: !pivot_last 1 2 3 <- All elements are separated by space'
    )
    async def pivot_last(self, ctx, *args):

        __data: list = []
        for elem in args:
            __data.append(int(elem))

        check_for_elements(__data, 2)

        def __high_partition(A: list, p: int, r: int) -> str:
            __result = ''
            x = A[r]
            i = p - 1
            for j in range(r):
                if A[j] <= x:
                    i = i + 1
                    A[i], A[j] = A[j], A[i]
            A[i + 1], A[r] = A[r], A[i + 1]
            __result = ' '.join((str(_) for _ in A))
            return __result

        await ctx.reply(make_reply(ctx, __high_partition(__data, 0, len(__data) - 1)))

    async def cog_command_error(self, ctx, error):
        print('debug -> ', error)
        if hasattr(error, 'original'):  # Handle other Exceptions

            if isinstance(error.original, ValueError):
                await ctx.reply(f'> {error.original}\n'
                                f'> Please check usage with !help command and try again')

        else:  # Handle errors that inherit from CommandError

            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.reply(f'> {error}\n'
                                f'> Please check usage with !help command and try again')

