import unittest
from datetime import datetime
from collections import defaultdict
from main import spend_points

class TestSpendPoints(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            ("DANNON", 1000, datetime(2020, 11, 2, 14, 0, 0)),
            ("UNILEVER", 200, datetime(2020, 10, 31, 11, 0, 0)),
            ("DANNON", -200, datetime(2020, 10, 31, 15, 0, 0)),
            ("MILLER COORS", 10000, datetime(2020, 11, 1, 14, 0, 0)),
            ("DANNON", 300, datetime(2020, 10, 31, 10, 0, 0)),
        ]

    def test_spend_points(self):
        expected = defaultdict(int, {'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300})
        result = spend_points(5000, self.transactions)
        self.assertEqual(result, expected)

    def test_not_spend_points(self):
        expected = defaultdict(int, {'DANNON': 1100, 'UNILEVER': 200, 'MILLER COORS': 10000})
        result = spend_points(0, self.transactions)
        self.assertEqual(result, expected)

    def test_not_enough_points(self):
        expected = defaultdict(int, {'DANNON': 1000, 'UNILEVER': 0,'MILLER COORS': 300})
        result = spend_points(10000, self.transactions)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
