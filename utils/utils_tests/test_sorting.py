import unittest

from utils.sorting import bubble_sort, insert_sort, select_sort, pivot_first, pivot_last


class TestBubbleSort(unittest.TestCase):
    def test_basic_cases(self):
        self.assertListEqual(
            [1, 2, 3, 4, 5], bubble_sort([5, 4, 3, 2, 1], 2, 5)[0]
        )
        self.assertEqual(
            f'5 4 3 2 1\n4 3 2 1 5\n3 2 1 4 5\n2 1 3 4 5\n1 2 3 4 5\n',
            bubble_sort([5, 4, 3, 2, 1], 2, 5)[1]
        )

    def test_errors(self):
        self.assertRaises(
            ValueError,
            bubble_sort, [5, 4, 3, 2, 1], 2, 3
        )

        self.assertRaises(
            ValueError,
            bubble_sort, [5, 4, 3, 2, 1], 10, 15
        )


class TestInsertSort(unittest.TestCase):
    def test_basic_case(self):
        self.assertListEqual(
            [1, 2, 3, 4, 5], insert_sort([5, 4, 3, 2, 1], 2, 5)[0]
        )

        self.assertEqual(
            '4 5 3 2 1\n3 4 5 2 1\n2 3 4 5 1\n1 2 3 4 5\n',
            insert_sort([5, 4, 3, 2, 1], 2, 5)[1]
        )

    def test_errors(self):
        self.assertRaises(
            ValueError,
            insert_sort, [5, 4, 3, 2, 1], 2, 3
        )

        self.assertRaises(
            ValueError,
            insert_sort, [5, 4, 3, 2, 1], 10, 15
        )


class TestSelectSort(unittest.TestCase):
    def test_basic_case(self):
        self.assertListEqual(
            [1, 2, 3, 4, 5], select_sort([5, 4, 3, 2, 1], 2, 5)[0]
        )

        self.assertEqual(
            '5 4 3 2 1\n1 4 3 2 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n',
            select_sort([5, 4, 3, 2, 1], 2, 5)[1]
        )

    def test_errors(self):
        self.assertRaises(
            ValueError,
            select_sort, [5, 4, 3, 2, 1], 2, 3
        )

        self.assertRaises(
            ValueError,
            select_sort, [5, 4, 3, 2, 1], 10, 15
        )


class TestPivotFirst(unittest.TestCase):
    def test_basic_cases(self):
        self.assertListEqual(
            [3, 5, 4, 1, 6, 8, 7, 9],
            pivot_first([7, 5, 4, 8, 6, 1, 3, 9], 2, 10)
        )

        self.assertListEqual(
            [5, 4, 1, 3, 8, 7, 9],
            pivot_first([7, 4, 1, 8, 3, 5, 9], 2, 15)
        )

        self.assertListEqual(
            [4, 5, 8, 2, 7, 11, 10, 13],
            pivot_first([10, 5, 8, 11, 7, 2, 4, 13], 2, 20)
        )

    def test_errors(self):
        self.assertRaises(
            ValueError,
            pivot_first, [5, 4, 3, 2, 1], 2, 3
        )

        self.assertRaises(
            ValueError,
            pivot_first, [5, 4, 3, 2, 1], 10, 15
        )


class TestPivotLast(unittest.TestCase):
    def test_basic_cases(self):
        self.assertListEqual(
            [5, 6, 7, 9, 12, 11, 16, 18, 10],
            pivot_last([5, 6, 16, 10, 12, 11, 7, 18, 9], 2, 15)
        )

        self.assertListEqual(
            [1, 4, 3, 5, 10, 12, 7, 15, 8, 6],
            pivot_last([1, 12, 7, 6, 10, 4, 3, 15, 8, 5], 2, 15)
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
