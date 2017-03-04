import unittest

from solution import *


class TextJustificationTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEquals(
            textJustification(
                ["This", "is", "an", "example", "of", "text", "justification."],
                16
            ),
            ["This    is    an", "example  of text", "justification.  "]
        )


if __name__ == '__main__':
    unittest.main()

