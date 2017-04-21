import unittest
import rangea

class TestApp(unittest.TestCase):
    def test_range(self):
        ra = rangea.RangeAnalyser()
        ra.analyse([
            {'numbers':[1, 2, 3, 4, 5]},
            {'numbers':[3, 2, 1, 4, 6]}
        ])

        self.assertEqual([0, 3], ra.check([4, 2, 3, 5, 5]))