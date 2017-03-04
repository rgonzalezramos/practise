
''' TESTS '''

import unittest
from solution import *


class ToAngleTestCase(unittest.TestCase):
    def test_q1(self):
        self.assertEquals(to_angle([1, 1]), 45)

    def test_q2(self):
        self.assertEquals(to_angle([-1, 1]), 135)

    def test_q3(self):
        self.assertEquals(to_angle([-1, -1]), 225)

    def test_q4(self):
        self.assertEquals(to_angle([1, -1]), 315)


class VisiblePointsTestCase(unittest.TestCase):
    def assertMatches(self, input_, output):
        self.assertEquals(visiblePoints(input_), output)

    def test_1(self):
        self.assertMatches(
           [[1, 1], [3, 1], [3, 2], [3, 3], [1, 3], [2, 5], [1, 5], [-1, -1], [-1, -2], [-2, -3], [-4, -4]],
            6
        )

    def test_2(self):
        self.assertMatches(
            [[3,0], [-2,2]],
            1
        )

if __name__ == '__main__':
    unittest.main()

