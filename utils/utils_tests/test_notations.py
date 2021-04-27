import unittest

from utils.notations import is_correct_theta


class TestIsCorrectTheta(unittest.TestCase):
    def test_base_cases(self):
        self.assertDictEqual(  # base case when all values are correct
            {'c1': True, 'c2': True, 'n0': True, 'summary': True
             }, is_correct_theta('1/3', '1', 3, 'n^2 - 2*n')
        )
        self.assertDictEqual(  # n0 is not correct
            {'c1': False, 'c2': True, 'n0': False, 'summary': False
             }, is_correct_theta('1/3', '1', -1, 'n^2 - 2*n')
        )
        self.assertDictEqual(  # c2 is not correct
            {'c1': True, 'c2': False, 'n0': True, 'summary': False
             }, is_correct_theta('1/3', '15', 3, 'n^2 - 2*n')
        )
        self.assertDictEqual(  # c1 is not correct
            {'c1': False, 'c2': True, 'n0': True, 'summary': False
             }, is_correct_theta('-89', '1', 3, 'n^2 - 2*n')
        )

    def test_wrong_input(self):
        self.assertDictEqual(  # base case when all values are correct
            {'c1': False, 'c2': True, 'n0': True, 'summary': False
             }, is_correct_theta('abcd', '1', 3, 'n^2 - 2*n')
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
