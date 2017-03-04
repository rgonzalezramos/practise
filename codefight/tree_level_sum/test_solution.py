import unittest

from solution import treeLevelSum

class TreeLevelSumTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEquals(
            treeLevelSum('(0(5(6()())(14()(9()())))(7(1()())(23()())))', 2),
            44
        )

if __name__ == '__main__':
    unittest.main()
