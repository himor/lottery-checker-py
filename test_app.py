import unittest
import rangea
import freqa
import builder

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

    def test_freq(self):
        fa = freqa.FrequencyAnalyser()
        fa.analyse([
            {'numbers':[1, 10, 20, 30, 55], 'mega':5},
            {'numbers':[1, 20, 30, 40, 60], 'mega':14},
            {'numbers':[10, 20, 30, 40, 60], 'mega':3}
            ])

        res = fa.check([1, 20, 30, 40, 60])
        self.assertEqual([], res, "Range Check failed - should be empty set " + str(res))

        res = set(fa.check([5, 20, 30, 40, 60]))
        self.assertEqual(set([0]), res, "Range Check failed - incorrect subset " + str(res))

        res = set(fa.check([1, 10, 20, 40, 60]))
        self.assertEqual(set([1, 2]), res, "Range Check failed - incorrect subset " + str(res))

        res = set(fa.check([5, 7, 25, 45, 75]))
        self.assertEqual(set([0, 1, 2, 3, 4]), res, "Range Check failed - incorrect subset " + str(res))

    def test_builder(self):
        b = builder.Builder()
        b.populate()

        self.assertEqual(len(b.numbers), 5, "Generated incorrect sequence")

        seq = b.get_numbers_string()
        text_seq = seq.split(" ")

        self.assertEqual(len(text_seq), 6, "Generated incorrect sequence with megaball")

