package main

import (
	"reflect"
	"sort"
	"testing"
)

func TestLetterCombinations(t *testing.T) {
	tests := []struct {
		name     string
		digits   string
		expected []string
	}{
		{
			name:     "Test case từ LeetCode example",
			digits:   "23",
			expected: []string{"ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"},
		},
		{
			name:     "Test case với empty string",
			digits:   "",
			expected: []string{},
		},
		{
			name:     "Test case với single digit",
			digits:   "2",
			expected: []string{"a", "b", "c"},
		},
		{
			name:     "Test case với digit 7",
			digits:   "7",
			expected: []string{"p", "q", "r", "s"},
		},
		{
			name:     "Test case với digit 9",
			digits:   "9",
			expected: []string{"w", "x", "y", "z"},
		},
		{
			name:     "Test case với three digits",
			digits:   "234",
			expected: []string{"adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"},
		},
		{
			name:     "Test case với digits 79",
			digits:   "79",
			expected: []string{"pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"},
		},
		{
			name:     "Test case với repeated digits",
			digits:   "22",
			expected: []string{"aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := letterCombinations(tt.digits)
			sort.Strings(result)
			sort.Strings(tt.expected)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("letterCombinations(%s) = %v, expected %v", tt.digits, result, tt.expected)
			}
		})
	}
}

func TestLetterCombinations_Length(t *testing.T) {
	tests := []struct {
		digits   string
		expected int
	}{
		{"234", 27},
		{"2345", 81},
		{"23456789", 11664},
	}

	for _, tt := range tests {
		result := letterCombinations(tt.digits)
		if len(result) != tt.expected {
			t.Errorf("letterCombinations(%s) length = %d, expected %d", tt.digits, len(result), tt.expected)
		}
	}
}

func BenchmarkLetterCombinations(b *testing.B) {
	digits := "23456789"
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		letterCombinations(digits)
	}
}
