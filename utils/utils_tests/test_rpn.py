import unittest

from utils.rpn import infix_to_postfix, postfix_eval


class TestInfixToPostfix(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(
            '2 7 + 3 / 14 3 - 4 * +',
            infix_to_postfix('( ( 2 + 7 ) / 3 + ( 14 - 3 ) * 4 )')
        )


class TestPostfixEval(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(
            '47.0',
            postfix_eval('2 7 + 3 / 14 3 - 4 * +', show_steps=False)
        )

        self.assertEqual(
            '2  | 2\n7  | 2 7\n+  | 9\n3  | 9 3\n/  | 3.0\n14 | 3.0 14\n3  | 3.0 14 3\n-  | 3.0 11\n4  | 3.0 11 4\n*  '
            '| 3.0 44\n+  | 47.0\n',
            postfix_eval('2 7 + 3 / 14 3 - 4 * +', show_steps=True)
        )
