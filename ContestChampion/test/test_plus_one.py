import unittest

from ContestChampion.contest.plus_one import BigInteger


class TestBigInteger(unittest.TestCase):
    def setUp(self) -> None:
        self.big_int = BigInteger()

    def test_plus_one_123(self):
        n1 = [1, 2, 3]
        result = self.big_int.plus_one_48ms(n1)
        self.assertEqual([1, 2, 4], result)

    def test_plus_one_9(self):
        n1 = [9]
        result = self.big_int.plus_one_48ms(n1)
        self.assertEqual([1, 0], result)

    def test_plus_one_9999(self):
        n1 = [9, 9, 9, 9]
        result = self.big_int.plus_one_48ms(n1)
        self.assertEqual([1, 0, 0, 0, 0], result)
    def test_plus_one_1089(self):
        n1 = [1,0,8,9]
        result = self.big_int.plus_one_48ms(n1)
        self.assertEqual([1,0,9,0], result)
