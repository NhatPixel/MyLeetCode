package main

import "math"

func threeSumClosest(nums []int, target int) int {
    r := 0
    d := math.MaxInt
    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {
            for k := j+1; k < len(nums); k++ {
                t := nums[i] + nums[j] + nums[k] 
                if t == target {
                    return t
                }
                td := abs(t-target)
                if td < d {
                    r = t
                    d = td
                }
            }
        }
    }
    return r
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}