import unittest

from utils.notations import is_correct_theta, calculate_theta


class TestCalculateTheta(unittest.TestCase):
    def test_base_case(self):
        self.assertTupleEqual(
            ('1/3', '1', '3'),
            calculate_theta('n**2 - 2*n')
        )

        self.assertTupleEqual(
            ('1/2', '2', '2'),
            calculate_theta('2*n**2 - 4*n + 2')
        )

        self.assertTupleEqual(
            ('5/4', '3', '2'),
            calculate_theta('3*n**2 - 4*n + 1')
        )


class TestIsCorrectTheta(unittest.TestCase):
    def test_base_cases(self):
        self.assertTupleEqual(  # base case when all values are correct
            (True, True, True),
            is_correct_theta('1/3', '1', 3, 'n^2 - 2*n')
        )
        self.assertTupleEqual(  # n0 is not correct
            (False, True, False),
            is_correct_theta('1/3', '1', -1, 'n^2 - 2*n')
        )
        self.assertTupleEqual(  # c2 is not correct
            (True, False, True),
            is_correct_theta('1/3', '15', 3, 'n^2 - 2*n')
        )
        self.assertTupleEqual(  # c1 is not correct
            (False, True, True),
            is_correct_theta('-89', '1', 3, 'n^2 - 2*n')
        )

    def test_wrong_input(self):
        self.assertTupleEqual(  # c1 wrong input
            (False, True, True), is_correct_theta('abcd', '1', 3, 'n^2 - 2*n')
        )

        self.assertTupleEqual(  # c2 wrong input
            (True, False, True), is_correct_theta('1/3', 'awdaw', 3, 'n^2 - 2*n')
        )

        self.assertTupleEqual(  # c1 and n0 wrong input
            (False, True, False), is_correct_theta('abcd', '1', -12, 'n^2 - 2*n')
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
