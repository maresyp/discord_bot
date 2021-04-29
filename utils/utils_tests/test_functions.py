import unittest

from utils.functions import sort_functions


class TestFunctionSort(unittest.TestCase):
    def test_basic_cases(self):
        self.assertListEqual(
            ['1', 'log(log(n))', 'log(n)**3', 'n*log(n)', 'n**(3/2)'],
            sort_functions(['n*log(n)', 'log(log(n))', 'log(n)**3', '1', 'n**(3/2)'], 2, 10)
        )

        self.assertListEqual(
            ['1', 'log(n)**3', 'n**(9/10)', 'n*log(n)', 'factorial(n)'],
            sort_functions(['n*log(n)', 'factorial(n)', 'log(n)**3', '1', 'n**(9/10)'], 2, 10)
        )

        self.assertListEqual(
            ['1', 'log(log(n))', 'log(n)**3', 'n**(3/2)', 'n**2'],
            sort_functions(['log(log(n))', '1', 'log(n)**3', 'n**2', 'n**(3/2)'], 2, 10)
        )


if __name__ == '__main__':
    unittest.main()
