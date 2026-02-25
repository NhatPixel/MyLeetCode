import unittest
import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("letter_combinations", Path(__file__).parent / "LetterCombinationsOfAPhoneNumber.py")
letter_combinations = importlib.util.module_from_spec(spec)
sys.modules["letter_combinations"] = letter_combinations
spec.loader.exec_module(letter_combinations)
Solution = letter_combinations.Solution


class TestLetterCombinationsOfAPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        digits = "23"
        result = self.solution.letterCombinations(digits)
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example2(self):
        digits = ""
        result = self.solution.letterCombinations(digits)
        self.assertEqual(result, [])
    
    def test_example3(self):
        digits = "2"
        result = self.solution.letterCombinations(digits)
        expected = ["a", "b", "c"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_single_digit_7(self):
        digits = "7"
        result = self.solution.letterCombinations(digits)
        expected = ["p", "q", "r", "s"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_single_digit_9(self):
        digits = "9"
        result = self.solution.letterCombinations(digits)
        expected = ["w", "x", "y", "z"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_three_digits(self):
        digits = "234"
        result = self.solution.letterCombinations(digits)
        self.assertEqual(len(result), 27)
        self.assertIn("adg", result)
        self.assertIn("cfi", result)
    
    def test_four_digits(self):
        digits = "2345"
        result = self.solution.letterCombinations(digits)
        self.assertEqual(len(result), 81)
    
    def test_with_seven(self):
        digits = "79"
        result = self.solution.letterCombinations(digits)
        expected = ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_all_digits(self):
        digits = "23456789"
        result = self.solution.letterCombinations(digits)
        self.assertEqual(len(result), 11664)
    
    def test_repeated_digits(self):
        digits = "22"
        result = self.solution.letterCombinations(digits)
        expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_leetcode_case1(self):
        digits = "23"
        result = self.solution.letterCombinations(digits)
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
