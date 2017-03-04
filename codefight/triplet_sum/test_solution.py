import unittest

from solution import *

class SolutionTestCase(unittest.TestCase):
    def test_1(self):
        self.assertFalse(
            tripletSum(15, [14, 1, 2, 3, 8, 15, 3]),
        )

    def test_2(self):
        self.assertTrue(
            tripletSum(8, [1, 1, 2, 5, 3])
        )

    def test_3(self):
        self.assertFalse(
            tripletSum(5, [2, 3, 1])
        )

    def test_4(self):
        self.assertTrue(
            tripletSum(165, [142, 712, 254, 869, 548, 645, 663, 758, 38, 860, 724, 742, 530, 779, 317, 36, 191, 843, 289, 107, 41, 943, 265, 649, 447, 806, 891, 730, 371, 351, 7, 102, 394, 549, 630, 624, 85, 955, 757, 841, 967, 377, 932, 309, 945, 440, 627, 324, 538, 539, 119, 83, 930, 542, 834, 116, 640, 659, 705, 931, 978, 307, 674, 387, 22, 746, 925, 73, 271, 830, 778, 574, 98, 513])
        )

    def test_9(self):
        self.assertTrue(
            tripletSum(1032, [493, 143, 223, 287, 65, 901, 188, 361, 414, 975, 271, 171, 236, 834, 712, 761, 897, 668, 286, 551, 141, 695, 696, 625, 20, 126, 577, 695, 659, 303, 372, 467, 679, 594, 852, 485, 19, 465, 120, 153, 801, 88, 61, 927, 11, 758, 171, 316, 577, 228, 44, 759, 165, 110, 883, 87, 566, 488, 578, 475, 626, 628, 630, 929, 424, 521, 903, 963, 124, 597, 738, 262, 196, 526, 265, 261, 203, 117, 31, 327, 12, 772, 412, 548, 154, 521, 791, 925, 189, 764, 941, 852, 663, 830, 901, 714, 959, 579, 366, 8, 478, 201, 59, 440, 304, 761, 358, 325, 478, 109, 114, 888, 802, 851, 461, 429, 994, 385, 406, 541, 112, 705, 836, 357, 73, 351])
        )

    def test_12(self):
        self.assertTrue(
            tripletSum(986, [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566, 560, 933])
        )

if __name__ == '__main__':
    unittest.main()

