import unittest
import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("three_sum_closest", Path(__file__).parent / "3SumClosest.py")
three_sum_closest = importlib.util.module_from_spec(spec)
sys.modules["three_sum_closest"] = three_sum_closest
spec.loader.exec_module(three_sum_closest)
Solution = three_sum_closest.Solution


class TestThreeSumClosest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example1(self):
        """Test case từ LeetCode example"""
        nums = [-1, 2, 1, -4]
        target = 1
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 2, "Tổng gần nhất với target=1 là 2 (-1+2+1)")
    
    def test_example2(self):
        """Test case với target = 0"""
        nums = [0, 0, 0]
        target = 1
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 0, "Tổng gần nhất là 0")
    
    def test_example3(self):
        """Test case với nhiều số âm"""
        nums = [-1, 0, 1, 2, -1, -4]
        target = 0
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 0, "Có thể tìm được tổng = 0")
    
    def test_exact_match(self):
        """Test case khi có tổng chính xác bằng target"""
        nums = [1, 2, 3, 4, 5]
        target = 6
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 6, "1+2+3 = 6 chính xác")
    
    def test_negative_target(self):
        """Test case với target âm"""
        nums = [-1, 2, 1, -4]
        target = -5
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, -4, "Tổng gần nhất với -5 là -4")
    
    def test_large_numbers(self):
        """Test case với số lớn"""
        nums = [100, 200, 300, 400, 500]
        target = 600
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 600, "100+200+300 = 600")
    
    def test_minimum_length(self):
        """Test case với mảng chỉ có 3 phần tử"""
        nums = [1, 2, 3]
        target = 10
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 6, "Chỉ có 1 tổng: 1+2+3=6")
    
    def test_all_negative(self):
        """Test case với tất cả số âm"""
        nums = [-5, -4, -3, -2, -1]
        target = -10
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, -10, "Tổng gần nhất: -5-4-1 = -10 (chính xác bằng target)")
    
    def test_mixed_positive_negative(self):
        """Test case với số dương và âm"""
        nums = [1, -3, 2, 4, -1, 0]
        target = 1
        result = self.solution.threeSumClosest(nums, target)
        self.assertIn(result, [0, 1, 2], "Kết quả phải là một trong các giá trị hợp lệ")
    
    def test_duplicate_numbers(self):
        """Test case với số trùng lặp"""
        nums = [1, 1, 1, 1, 1]
        target = 0
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, 3, "1+1+1 = 3")
    
    def test_leetcode_case1(self):
        """Test case từ LeetCode"""
        nums = [1, 1, -1, -1, 3]
        target = -1
        result = self.solution.threeSumClosest(nums, target)
        self.assertEqual(result, -1, "Có thể tìm được tổng = -1")


if __name__ == '__main__':
    unittest.main()
