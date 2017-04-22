import unittest
import rangea

class TestApp(unittest.TestCase):
    def test_range(self):
        ra = rangea.RangeAnalyser()
        ra.analyse([
            {'numbers':[1, 2, 3, 4, 5]},
            {'numbers':[2, 2, 1, 4, 6]},
            {'numbers':[3, 2, 1, 4, 6]}
        ])

        self.assertEqual({"min": 1, "max": 3}, ra.cache[1], "Range Analyse failed")
        self.assertEqual({"min": 2, "max": 2}, ra.cache[2], "Range Analyse failed")
        self.assertEqual({"min": 1, "max": 3}, ra.cache[3], "Range Analyse failed")
        self.assertEqual({"min": 4, "max": 4}, ra.cache[4], "Range Analyse failed")
        self.assertEqual({"min": 5, "max": 6}, ra.cache[5], "Range Analyse failed")

        self.assertEqual([0, 3], ra.check([4, 2, 3, 5, 5]), "Range Check failed")
        self.assertEqual([1, 2, 4], ra.check([3, 4, 7, 4, 0]), "Range Check failed")
