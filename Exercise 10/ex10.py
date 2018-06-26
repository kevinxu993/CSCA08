from a2 import *
import unittest


class TestSetByPos(unittest.TestCase):

    def test_01_set_returns_none(self):
        subject1 = Female('test_subject_1')
        # try setting by position
        result = subject1.set_by_pos(1, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")

    def test_02_get_returns_gene(self):
        subject2 = Female('test_subject_2')
        # try setting by position
        subject2.set_by_pos(1, 5, 'AT')
        # try getting by position
        result = subject2.get_by_pos(1, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's returning the gene
        expected = 'AT'
        self.assertEqual(result, expected,
                         "get_by_pos should be returning the gene that has " +
                         "been set")

    def test_03_set_returns_none(self):
        subject3 = Female('test_subject_3')
        # try setting a marker
        result = subject3.set_marker('abc', 1, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_marker shouldn't be returning anything")

    def test_04_set_returns_none(self):
        subject4 = Female('test_subject_4')
        # try setting a marker
        subject4.set_marker('abc', 1, 5)
        # try setting by a marker
        result = subject4.set_by_marker('abc', 'GC')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_marker shouldn't be returning anything")

    def test_05_get_returns_gene(self):
        subject5 = Female('test_subject_5')
        # try setting a marker
        subject5.set_marker('abc', 1, 5)
        # try setting by a marker
        subject5.set_by_marker('abc', 'GC')
        # try getting by a marker
        result = subject5.get_by_marker('abc')
        # if we got this far, we know it at least didn't crash
        # now also check that it's returning the gene
        expected = 'GC'
        self.assertEqual(result, expected,
                         "get_by_marker should be returning the gene that " +
                         "has been set")

if(__name__ == "__main__"):
    unittest.main(exit=False)
