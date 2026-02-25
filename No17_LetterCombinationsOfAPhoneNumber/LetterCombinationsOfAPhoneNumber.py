from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz", # 9
        ]

        result: List[str] = []
        idx = [0] * len(digits)

        while True:
            buf = []
            for i, v in enumerate(idx):
                m = letters[ord(digits[i]) - ord('0')]
                buf.append(m[v])
            result.append("".join(buf))

            i = len(idx) - 1
            while i >= 0:
                m = letters[ord(digits[i]) - ord('0')]
                idx[i] += 1
                if idx[i] < len(m):
                    break
                idx[i] = 0
                i -= 1

            if i < 0:
                break

        return result