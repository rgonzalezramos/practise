import unittest

from solution import swapLexOrder, str_swap


class SwapLexOrderTestCase(unittest.TestCase):
    def test_case1(self):
        self.assertEquals(
            swapLexOrder("abdc", [[1, 4], [3, 4]]),
            "dbca"
        )

    def test_performance(self):
        self.assertEquals(
            swapLexOrder(
                "fixmfbhyutghwbyezkveyameoamqoi",
                [[8,5], [10,8], [4,18], [20,12], [5,2], [17,2], [13,25], [29,12], [22,2], [17,11]]
            ),
            "fzxmybhtuigowbyefkvhyameoamqei"
        )


class StrSwapTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEquals(
            str_swap('hello', 1, 2),
            'hlelo'
        )


if __name__ == '__main__':
    unittest.main()

