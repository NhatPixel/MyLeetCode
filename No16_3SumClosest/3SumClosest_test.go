package main

import "testing"

func TestThreeSumClosest(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		target   int
		expected int
	}{
		{
			name:     "Test case từ LeetCode example",
			nums:     []int{-1, 2, 1, -4},
			target:   1,
			expected: 2,
		},
		{
			name:     "Test case với target = 0",
			nums:     []int{0, 0, 0},
			target:   1,
			expected: 0,
		},
		{
			name:     "Test case với nhiều số âm",
			nums:     []int{-1, 0, 1, 2, -1, -4},
			target:   0,
			expected: 0,
		},
		{
			name:     "Test case khi có tổng chính xác bằng target",
			nums:     []int{1, 2, 3, 4, 5},
			target:   6,
			expected: 6,
		},
		{
			name:     "Test case với target âm",
			nums:     []int{-1, 2, 1, -4},
			target:   -5,
			expected: -4,
		},
		{
			name:     "Test case với số lớn",
			nums:     []int{100, 200, 300, 400, 500},
			target:   600,
			expected: 600,
		},
		{
			name:     "Test case với mảng chỉ có 3 phần tử",
			nums:     []int{1, 2, 3},
			target:   10,
			expected: 6,
		},
		{
			name:     "Test case với tất cả số âm",
			nums:     []int{-5, -4, -3, -2, -1},
			target:   -10,
			expected: -10,
		},
		{
			name:     "Test case với số trùng lặp",
			nums:     []int{1, 1, 1, 1, 1},
			target:   0,
			expected: 3,
		},
		{
			name:     "Test case từ LeetCode",
			nums:     []int{1, 1, -1, -1, 3},
			target:   -1,
			expected: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := threeSumClosest(tt.nums, tt.target)
			if result != tt.expected {
				t.Errorf("threeSumClosest(%v, %d) = %d, expected %d", tt.nums, tt.target, result, tt.expected)
			}
		})
	}
}

func TestThreeSumClosest_MixedPositiveNegative(t *testing.T) {
	nums := []int{1, -3, 2, 4, -1, 0}
	target := 1
	result := threeSumClosest(nums, target)
	
	validResults := map[int]bool{0: true, 1: true, 2: true}
	if !validResults[result] {
		t.Errorf("threeSumClosest(%v, %d) = %d, expected one of [0, 1, 2]", nums, target, result)
	}
}

func BenchmarkThreeSumClosest(b *testing.B) {
	nums := []int{-1, 2, 1, -4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
	target := 1
	
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		threeSumClosest(nums, target)
	}
}
