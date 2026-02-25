package main

func letterCombinations(digits string) []string {
    if len(digits) == 0 {
        return []string{}
    }
    
    letters := []string{
        " ",     // 0
        "",      // 1
		"abc",   // 2
		"def",   // 3
		"ghi",   // 4
		"jkl",   // 5
		"mno",   // 6
		"pqrs",  // 7
		"tuv",   // 8
		"wxyz",  // 9
	}

    result := []string{}
    idx := make([]int, len(digits))
    for {
		buf := make([]byte, len(digits))
		for i, v := range idx {
			m := letters[int(digits[i]-'0')]
			buf[i] = m[v]
		}
		result = append(result, string(buf))

        i := len(digits) - 1
        for i >= 0 {
            idx[i]++
            if idx[i] < len(letters[int(digits[i]-'0')]) {
                break
            }
            idx[i] = 0
            i--
        }

        if i < 0 {
            break
        }
    }
    return result
}